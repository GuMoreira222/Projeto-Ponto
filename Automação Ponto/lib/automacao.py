from datetime import datetime, timedelta
from tkinter import messagebox
import schedule
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import pyautogui
from time import sleep
from lib.tratar_env import retorna_env

# Função que confirma se o usuário deseja bater o ponto
def confirmacao():
    hora = datetime.now()
    hora_formatada = hora.strftime("%H:%M")
    confirmar = pyautogui.confirm(f"Já é {hora_formatada}\nDeseja bater o ponto?", buttons = ['SIM', 'NÃO'])
    return confirmar

def esperar_elemento_clicavel(driver, by_method, element, timeout=25):
    elemento = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by_method, element)))
    return elemento

def esperar_elemento_aparecer(driver, by_method, element, timeout=25):
    elemento = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_method, element)))
    return elemento

# Função que bate o ponto com selenium
def bater_ponto(user, password):
    
    try:

        servico = Service(ChromeDriverManager().install())
        
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--headless=new")

        driver = webdriver.Chrome(service=servico, options=opcoes)

        driver.get("http://sicoobsc139565.protheus.cloudtotvs.com.br:1404/meurh01/#/login")
        driver.maximize_window()

        sleep(2)
        campo_user = esperar_elemento_aparecer(driver, By.XPATH, "/html/body/app-root/div/div/app-login/div[1]/div[1]/form/po-input/po-field-container/div/div[2]/input")
        campo_user.send_keys(user)
        sleep(2)
        campo_senha = esperar_elemento_aparecer(driver, By.XPATH, "/html/body/app-root/div/div/app-login/div[1]/div[1]/form/po-password/po-field-container/div/div[2]/input")
        campo_senha.send_keys(password)
        sleep(2)
        botao_entrar = esperar_elemento_clicavel(driver, By.XPATH, "/html/body/app-root/div/div/app-login/div[1]/div[1]/form/po-button[1]/button")
        botao_entrar.click()
        sleep(2)
        menu_ponto = esperar_elemento_aparecer(driver, By.XPATH, "/html/body/app-root/div/div/div[2]/po-menu/div[2]/nav/div/div/div[3]/po-menu-item/div/div[1]")
        menu_ponto.click()
        sleep(2)
        op_bater_ponto = esperar_elemento_clicavel(driver, By.XPATH, "/html/body/app-root/div/div/div[2]/po-menu/div[2]/nav/div/div/div[3]/po-menu-item/div/div[2]/div[3]/po-menu-item/a/div")
        op_bater_ponto.click()
        sleep(2)
        fechar_pop_up = esperar_elemento_clicavel(driver, By.XPATH, "/html/body/app-root/div/div/div[2]/po-page-default/po-page/div/po-page-content/div/app-clocking-geo-register/po-modal[1]/div/div/div/div/div/div[2]/div/button")
        fechar_pop_up.click()
        sleep(2)

        botao_ponto = esperar_elemento_clicavel(driver, By.XPATH, "/html/body/app-root/div/div/div[2]/po-page-default/po-page/div/po-page-content/div/app-clocking-geo-register/div/div[1]/div[1]/div/app-swipe-button/div/div/div/div")
        acoes = ActionChains(driver)
        acoes.double_click(botao_ponto).perform()

        hora = datetime.now()
        hora_formatada = hora.strftime("%H:%M")
        messagebox.showinfo("AVISO", f"Ponto batido às {hora_formatada}. Não esqueça de conferir seu espelho de ponto mais tarde!")
        sleep(2)

    except TimeoutException as e:
        messagebox.showerror("ERRO", f"Tempo limite excedido: {e}")
    except WebDriverException as e:
        messagebox.showerror("ERRO", f"Erro no Web Driver: {e}")
    except NoSuchElementException as e:
        messagebox.showerror("ERRO", f"Elemento não encontrado: {e}")
    except:
        messagebox.showerror("ERRO", "Erro desconhecido")

# Função que programa os horários para bater o ponto
def programar_horario(login, lista_horas):

    try:
        
        batida_final = datetime.strptime(lista_horas[3], "%H:%M")
        batida_final_formatada = batida_final.strftime("%H:%M")

        for hr in lista_horas:
            
            hora = datetime.strptime(hr, "%H:%M")
            hora_format = hora.strftime("%H:%M")
            hora_atual = datetime.now()
            hora_atual_format = hora_atual.strftime("%H:%M")

            if hora_format < hora_atual_format and hora_format != lista_horas[3]:
                continue
                
            while hora_atual_format < batida_final_formatada:
                
                while hora_atual_format < hora_format:
                    sleep(60)
                    hora_atual = datetime.now()
                    hora_atual_format = hora_atual.strftime("%H:%M")

                confirmar = confirmacao()
                if confirmar == "SIM":
                    bater_ponto(login[0], login[1])
                    break
                    
                ponto_batido = pyautogui.confirm(f"Já bateu seu ponto das {hr}", buttons = ['SIM', 'NÃO'])
                
                if ponto_batido == "SIM":
                    break

                if hora_format == batida_final_formatada:
                    hora_atual = datetime.now()
                    hora_atual_format = hora_atual.strftime("%H:%M")
                    
                    if batida_final_formatada < hora_atual_format:
                        batida_final = datetime.strptime(hora_atual, "%H:%M")
                    
                    batida_final += timedelta(minutes=10)
                    batida_final_formatada = batida_final.strftime("%H:%M")
                    
                else:
                    hora_atual = datetime.now()
                    hora_atual_format = hora_atual.strftime("%H:%M")
                    
                    if hora_atual_format > hora_format:
                        hora = datetime.strptime(hora_atual, "%H:%M")
                    
                    hora += timedelta(minutes=10)
                    hora_format = hora.strftime("%H:%M")
                                    
    except ValueError:
        messagebox.showerror("ERRO", "Erro na conversão ou comparação das datas")

def iniciar_automacao():
    login, lista_horas = retorna_env()
    programar_horario(login, lista_horas)