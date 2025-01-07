from selenium import webdriver

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotInteractableException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import openpyxl

## Partie 1 : Constitution de la base de donnée.

sites = [
    "1% pour la planète",
    "Akuo Foundation",
    "Concours Green Link",
    "Danone",
    "Fape Engie",
    "FFB",
    "Fondation Abalone",
    "Fondation AccorHotel",
    "Fondation AG2R La Mondiale",
    "Fondation Air Liquide",
    "Fondation Alstom",
    "Fondation Amar y Servir",
    "Fondation Artelia",
    "Fondation Autonomia",
    "Fondation Bardon",
    "Fondation Batigère",
    "Fondation Baudoux",
    "Fondation Biocoop",
    "Fondation BNP Paribas",
    "Fondation Bonduelle",
    "Fondation Brageac",
    "Fondation Carasso",
    "Fondation Caritas France",
    "Fondation Cassiopée",
    "Fondation Crédit Agricole Pays de France",
    "Fondation de France",
    "Fondation Denis & Fils",
    "Fondation Du Lucq",
    "Fondation du Patrimoine",
    "Fondation Ecotone",
    "Fondation Eiffage",
    "Fondation Ekibio",
    "Fondation Enovos",
    "Fondation Fondation Georges Truffaut",
    "Fondation GRDF",
    "Fondation Groupe LDLC",
    "Fondation Groupe Pierre et Vacances",
    "Fondation Hermes",
    "Fondation Humus",
    "Fondation Aubert Duval",
    "Fondation Julienne Dumeste",
    "Fondation Léa Nature",
    "Fondation Lemarchand / Nature et Découverte",
    "Fondation M6",
    "Fondation MACIF",
    "Fondation Maisons du Monde",
    "Fondation Michelin",
    "777 Children",
    "Fondation Oak",
    "Fondation Orcom",
    "Fondation Palatine",
    "Fondation Patagonia",
    "Fondation Puressentiel",
    "Fondation RAJA",
    "Fondation RATP",
    "Fondation Rexel",
    "Fondation RTE",
    "Fondation Saint-Gobain",
    "Fondation Schneider Electric",
    "Fondation Setec",
    "Fondation Société générale",
    "Fondation Terre Solidaire",
    "Fondation UEM",
    "Fondation Vinci pour la cité",
    "Fondation Watts for Change",
    "Fonds de dotation Jean Baudelet",
    "Fonds de dotation terre et fils",
    "Fonds Entreprendre&+",
    "Fonds Le Chant des Étoiles",
    "Klorane Botanical Foundation",
]

urls = [
    "https://www.onepercentfortheplanet.fr",
    "https://www.akuoenergy.com/la-fondation-akuo",
    "https://www.green-link.org/",
    "https://institutdanone.org/",
    "https://www.engie.com/FAPE",
    "https://www.ffbatiment.fr",
    "https://abalone-fondation.org",
    "https://group.accor.com/fr-FR/commitment/collective-force/endowment-fund",
    "https://www.ag2rlamondiale.fr/fondation-d-entreprise/la-fondation",
    "https://www.fondationairliquide.com/fr",
    "https://www.foundation.alstom.com",
    "https://fondation-amaryservir.org",
    "https://fondationartelia.org/fr",
    "https://fondationautonomia.org",
    "https://fondation-bardon.com/",
    "http://www.fondation-batigere.fr",
    "http://www.fondationbaudoux.fr",
    "https://www.biocoop.fr/",
    "https://group.bnpparibas/nos-engagements/fondation-bnp-paribas",
    "https://www.fondation-louisbonduelle.org/presentation-de-la-fondation/",
    "https://fondationbrageac.org",
    "https://www.fondationcarasso.org",
    "https://www.fondationcaritasfrance.org/",
    "https://www.fondationcassiopee.org/fr/",
    "https://fondation-ca-paysdefrance.org",
    "https://www.fondationdefrance.org/fr/",
    "https://www.bougies-denis.com/fondation-denis-fils/",
    "https://www.fondationdefrance.org/fr/annuaire-des-fondations/fondation-du-lucq",
    "https://www.fondation-patrimoine.org",
    "https://www.ecotone.bio/fr/notre-fondation",
    "https://www.eiffage.com/groupe/presentation-de-la-fondation-eiffage",
    "https://www.ekibio.fr/la-fondation",
    "https://www.fondation-enovos.lu/fr/",
    "https://www.fondation-georges-truffaut.org",
    "https://fondationgrdf.fr",
    "https://www.fondation-groupe-ldlc.org",
    "https://www.groupepvcp.com/engagement/notre-fondation/",
    "https://www.fondationdentreprisehermes.org/fr",
    "https://www.fondation-humus.com",
    "https://www.fondationaubertduval.org/",
    "https://fondationjuliennedumeste.fr",
    "https://fondation-mecenat-leanature.org",
    "https://www.fondationlemarchand.org/presentation",
    "https://www.groupem6.fr/engagements/la-fondation/",
    "https://www.fondation-macif.org",
    "https://foundation.maisonsdumonde.com",
    "https://fondation.michelin.com",
    "https://777children.fr",
    "https://oakfnd.org",
    "https://fondation.orcom.fr",
    "https://www.palatine.fr/votre-banque/nos-engagements/partenariats-mecenats/",
    "https://eu.patagonia.com/fr/fr/how-we-fund/",
    "https://fr.puressentiel.com/pages/fondation-puressentiel",
    "https://www.fondation-raja-marcovici.com",
    "https://ratpgroup.com/fr/le-groupe-ratp/fondation-groupe-ratp/",
    "https://www.rexelfoundation.com/fr",
    "https://fondation-rte.org",
    "https://fondation.saint-gobain.com",
    "https://www.se.com/fr/fr/about-us/sustainability/foundation/",
    "https://fondationsetec.org",
    "https://fondation.societegenerale.com/fr",
    "https://fondation-terresolidaire.org",
    "https://www.fondation-uem.org",
    "https://www.fondation-vinci.com",
    "https://www.wattforchange.org",
    "https://fondsjeanbaudelet.fr",
    "https://terreetfils.org/ecosysteme/fonds-de-dotation/",
    "https://www.entreprendreetplus.org",
    "https://unespritdefamille.org/membre/le-chant-des-etoiles/",
    "https://www.kloranebotanical.foundation",
]

df = pd.DataFrame()

df["Fondations"] = sites
df["Urls"] = urls
df["Texte"] = [None] * len(sites)


class Scraping:
    cpt_site = -1

    def __init__(self):
        Scraping.cpt_site += 1
        self.cpt_site = Scraping.cpt_site
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click_cookies(self):
        pass

    def scrape_text(self):
        pass

    def close_browser(self):
        self.driver.quit()


class PourLaPlanete(Scraping):
    def __init__(self):
        super().__init__()

        self.site_url = "https://www.onepercentfortheplanet.fr/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = "//*[@class='cmplz-btn cmplz-accept cc-allow cc-btn']"
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div"
            ).text
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="custom_html-3"]/div/p/a'
                ).text
            )
            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AkuoFoundation(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.akuoenergy.com/la-fondation-akuo"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(1)
            cookie_button_ID = "tarteaucitronPersonalize2"
            cookie_button = self.driver.find_element(By.ID, cookie_button_ID)
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):

        try:
            about = self.driver.find_element(
                By.XPATH, '//*[@id="block-menu-main"]/ul/li[2]/a'
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            textes = self.driver.find_element(
                By.XPATH, '//*[@id="block-frontend-content"]/article/div/div'
            )
            clean_text = re.sub(r"En savoir plus", "", textes.text)

            info_financement = self.driver.find_element(
                By.XPATH,
                '//*[@id="block-frontend-content"]/article/div/div/section[2]/div/div/div[1]/div/div[2]/div/a',
            )
            new_url = info_financement.get_attribute("href")
            self.driver.get(new_url)

            clean_text += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="block-frontend-content"]/article/div/div/section[1]/div/div/div[1]/div/div/div',
                ).text
                + "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="block-blocfooter"]/div/blockquote/p/span/a/span'
                ).text
            )

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class ConcoursGreenLink(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.green-link.org/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            about = self.driver.find_element(By.XPATH, '//*[@id="menu-item-482"]/a')
            new_url = about.get_attribute("href")
            self.driver.get(new_url)

            texte = (
                self.driver.find_element(By.XPATH, '//*[@id="post-17"]').text
                + "\n"
                + self.driver.find_element(By.XPATH, '//*[@id="footer"]/div').text
            )
            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Danone(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://institutdanone.org/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="popin_tc_privacy_button_2"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/a'
            ).click()
            texte = (
                self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div[1]'
                ).text
                + "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/div[3]/div[2]/div'
                ).text
                + "\n"
                + self.driver.find_element(By.XPATH, '//*[@id="main"]/div[4]').text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class FapeEngie(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.engie.com/FAPE"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = (
                '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
            )
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(1)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/p[2]"
            ).text

            self.driver.find_element(
                By.XPATH, '//*[@id="readingProgress-part-1"]/div[1]'
            ).click()
            sleep(2)
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="readingProgress-part-1"]/div[2]/div/div[2]/div/div/div',
                ).text
            )

            self.driver.find_element(
                By.XPATH, '//*[@id="readingProgress-part-3"]/div[1]'
            ).click()
            sleep(1)

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="readingProgress-part-3"]/div[2]/div/div[2]/div/div/div',
                ).text
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="readingProgress-part-3"]/div[2]/div/div[2]/div/div',
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class FFB(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.ffbatiment.fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(7)
            cookie_button_xpath = '//*[@id="onetrust-close-btn-container"]/button'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="content"]/div/section[4]/div/div/div/div/div/div/div[2]/div/div[1]/div',
            ).text

            self.driver.find_element(
                By.XPATH,
                '//*[@id="content"]/div/section[4]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/a',
            ).click()

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="representer"]/div/div[2]/div/section/div/div/div[2]/div/div/div/div[2]/div/div/div',
                ).text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="defendre"]/div/div[2]/div/section[1]/div/div'
                ).text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="defendre"]/div/div[2]/div/section[1]/div/div/div[2]/div/div',
                ).text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="promouvoir"]/div/div[2]/div/section/div/div/div[2]/div/div',
                ).text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="communiquer"]/div/div[2]/div/section[1]/div/div/div[2]/div/div',
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Abalone(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://abalone-fondation.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="cookie_action_close_header"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="nav-item-49"]/a').click()
            sleep(2)
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="post-16"]',
            ).text

            self.driver.find_element(By.XPATH, '//*[@id="nav-item-47"]/a').click()
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="nav-item-102"]/a').click()

            texte += (
                "\n"
                + self.driver.find_element(By.XPATH, '//*[@id="post-100"]/div[4]').text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AccorHotel(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = (
            "https://group.accor.com/fr-FR/commitment/collective-force/endowment-fund"
        )

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="main"]/div[1]/article/div[2]',
            ).text

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AG2RLaMondiale(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = (
            "https://www.ag2rlamondiale.fr/fondation-d-entreprise/la-fondation"
        )

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="popin_tc_privacy_button_2"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="6a5599a7-c9a6-45d1-b73f-66d73cc423dc"]',
            ).text

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="3f01f4cf-5c5c-4954-bd6c-9bf6027fb60a"]/div/div[2]/div',
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AirLiquide(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationairliquide.com/fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="didomi-notice-agree-button"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="p19341"]/p',
            ).text

            # 1
            self.driver.find_element(
                By.XPATH,
                '//*[@id="p23026"]/div[2]/div[1]/a/span',
            ).click()

            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="p19441"]/p').text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="p19836"]/div/div[2]'
                ).text
            )

            self.driver.find_element(
                By.XPATH,
                '//*[@id="breadcrumb"]/ol/li[1]/a/span',  # Retour à l'accueil
            ).click()

            # 2
            self.driver.find_element(
                By.XPATH,
                '//*[@id="p23026"]/div[2]/div[2]/a/span',
            ).click()

            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="p19486"]/p').text
            )
            texte += "\n" + self.driver.find_element(By.XPATH, '//*[@id="p19941"]').text

            self.driver.find_element(
                By.XPATH,
                '//*[@id="breadcrumb"]/ol/li[1]/a/span',
            ).click()

            # 3
            self.driver.find_element(
                By.XPATH,
                '//*[@id="p23026"]/div[2]/div[3]/a/span',
            ).click()

            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="p21841"]/p').text
            )
            texte += "\n" + self.driver.find_element(By.XPATH, '//*[@id="p21846"]').text

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Alstom(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.foundation.alstom.com"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="block-alstom-contenudelapageprincipale"]/div/article/section[6]/div[1]/div/div[2]/div[1]/p',
            ).text

            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="block-alstom-contenudelapageprincipale"]/div/article/section[5]/div/div/div/div/div/p[1]',
            ).text

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="block-alstom-contenudelapageprincipale"]/div/article/section[2]',
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AmaryServir(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-amaryservir.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:

            about = self.driver.find_element(By.XPATH, '//*[@id="menu-item-6975"]/a')
            new_url = about.get_attribute("href")
            self.driver.get(new_url)

            texte = self.driver.find_element(
                By.XPATH,
                '//*[@id="main"]/div[2]',
            ).text

            about = self.driver.find_element(By.XPATH, '//*[@id="menu-item-464"]/a')
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="main"]/div[2]',
                ).text
            )

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="av_section_1"]/div/div/div/div/div/a[2]/span[2]',
                ).text
            )

            self.driver.find_element(
                By.XPATH, '//*[@id="menu-item-5777"]/a/span[2]'
            ).click()

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH,
                    '//*[@id="main"]/div/div/main/div/div/div[1]/section/div',
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Artelia(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationartelia.org/fr/la-fondation/presentation"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="popup-buttons"]/button[1]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, "/html/body/div[2]/div[3]/div"
            ).text

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Autonomia(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationautonomia.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = (
                '//*[@id="moove_gdpr_cookie_info_bar"]/div/div/div[2]/button[1]'
            )
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="home"]/header/div[1]/p'
            ).text

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="article"]/section[2]/div[1]/p'
                ).text
            )

            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="article"]/section[4]/div[1]'
                ).text
            )

            about = self.driver.find_element(
                By.XPATH, '//*[@id="article"]/section[4]/div[2]/article[1]/div/a'
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="article"]').text
            )

            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="article"]/section[4]/div[2]/article[2]/div/a'
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)

            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="article"]').text
            )

            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="article"]/section[4]/div[2]/article[3]/div/a'
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte += (
                "\n" + self.driver.find_element(By.XPATH, '//*[@id="article"]').text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Bardon(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-bardon.com/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="menu-item-27"]/a').click()
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="post-17"]/div/div/div[1]'
            ).text

            self.driver.find_element(By.XPATH, '//*[@id="menu-item-6582"]/a').click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="post-15"]/div/div/div[3]/div/div'
                ).text
            )
            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Batigère(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "http://www.fondation-batigere.fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = "/html/body/div[5]/div/a[2]"
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="menu-item-17"]/a').click()
            texte = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]").text

            self.driver.find_element(By.XPATH, '//*[@id="menu-item-18"]/a').click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/div/section"
                ).text
            )
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/div/aside/ul"
                ).text
            )
            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Baudoux(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "http://www.fondationbaudoux.fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, "/html/body/div/table[2]/tbody/tr/td[5]/div"
            ).text

            self.driver.find_element(
                By.XPATH,
                "/html/body/div/table[2]/tbody/tr/td[2]/table/tbody/tr[4]/td/a",
            ).click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div/table[2]/tbody/tr/td[5]/div"
                ).text
            )

            self.driver.find_element(
                By.XPATH,
                "/html/body/div/table[2]/tbody/tr/td[2]/table/tbody/tr[6]/td/a",
            ).click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div/table[2]/tbody/tr/td[5]/div"
                ).text
            )

            self.driver.find_element(
                By.XPATH,
                "/html/body/div/table[2]/tbody/tr/td[2]/table/tbody/tr[8]/td/a",
            ).click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div/table[2]/tbody/tr/td[5]/div"
                ).text
            )

            self.driver.find_element(
                By.XPATH,
                "/html/body/div/table[2]/tbody/tr/td[2]/table/tbody/tr[10]/td/a",
            ).click()
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, "/html/body/div/table[2]/tbody/tr/td[5]/div"
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Biocoop(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.biocoop.fr/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="html-body"]/div[1]/header/div[2]/div/div/div/div[2]/div/div[2]/ul/li[2]/div/div/ul/li[2]/a',
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]').text

            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="html-body"]/div[1]/header/div[2]/div/div/div/div[2]/div/div[2]/ul/li[3]/div/div/ul/li[6]/a',
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="maincontent"]/div[2]/div'
                ).text
            )

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class BNPParibas(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://group.bnpparibas/nos-engagements/fondation-bnp-paribas"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_xpath = '//*[@id="accept-recommended-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(By.XPATH, '//*[@id="main"]').text

            print(texte)
            df.at[self.cpt_site, "Texte"] = texte
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class LouisBonduelle(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = (
            "https://www.fondation-louisbonduelle.org/presentation-de-la-fondation/"
        )

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.ID, "page")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Brageac(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationbrageac.org"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.ID, "main")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Carasso(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationcarasso.org"

    def click_cookies(self):
        self.driver.get(self.site_url)
        bouton_xpath_cookie = (
            '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]'
        )
        click_cookie = self.driver.find_element(By.XPATH, bouton_xpath_cookie).click()
        sleep(2)

    def scrape_text(self):
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div[1]/ul/li[1]'
            ).click()
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="fundation"]/div/section[2]'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)

            self.driver.find_element(
                By.XPATH, '//*[@id="header"]/div[1]/div/div/div[2]/div[1]/ul/li[4]'
            ).click()
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="calls"]/div/section[2]'
            )
            clean_text += "\n" + re.sub(r"^\s+", "", texte.text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print(clean_text)
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Caritas(Scraping):

    BUTTON_FONDATION_XPATH = "/html/body/header/div/nav/div/div/ul/li[1]"

    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationcaritasfrance.org/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button_Xpath = '//*[@id="c-p-bn"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_Xpath)
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            actions = ActionChains(self.driver)
            self.driver.get(self.site_url)
            self.driver.find_element(By.XPATH, self.BUTTON_FONDATION_XPATH).click()

            # Descriptif Fondation
            a_propos_fondation = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/article/section'
            ).text
            clean_text = re.sub(r"^\s+", "", a_propos_fondation)

            # Descriptif financement
            self.driver.find_element(
                By.XPATH, "/html/body/header/div/nav/div/div/ul/li[3]"
            ).click()
            a_propos_financement = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/article'
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos_financement)

            # Simuler un clic droit sur la bannière principale
            actions.context_click(
                self.driver.find_element(
                    By.XPATH, "/html/body/header/div/nav/div/div/ul/li[3]"
                )
            ).perform()
            new_url = self.driver.find_element(
                By.XPATH, "/html/body/header/div/nav/div/div/ul/li[3]/ul/li[6]/a"
            ).get_attribute("href")
            self.driver.get(new_url)

            # Descriptif projet
            a_propos_projet = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/article/section[2]'
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos_projet)

            # CONTACT
            self.driver.find_element(
                By.XPATH, "/html/body/header/div/nav/div/div/ul/li[6]"
            ).click()

            text_contact = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/article/section[1]/div/div/div'
            ).text
            url_contact = (
                self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/article/section[1]/div/div/div/p[2]'
                )
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            clean_text += "\n" + re.sub(r"^\s+", "", text_contact)
            clean_text += "\n" + re.sub(r"^\s+", "", url_contact)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Cassiopee(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationcassiopee.org/fr/"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div')
            clean_text1 = re.sub(r"^\s+", "", texte.text)
            sleep(3)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="top"]/div/nav/div[2]/ul'
            ).find_element(By.TAG_NAME, "a")
            link = about.get_attribute("href")
            self.driver.get(link)
            texte = self.driver.find_element(By.ID, "content")
            clean_text2 = re.sub(r"^\s+", "", texte.text)
            clean_text = clean_text1 + clean_text2
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class PaysDeFrance(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-ca-paysdefrance.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]',
                    )
                )
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(By.ID, "menu-item-572").find_element(
                By.TAG_NAME, "a"
            )
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(By.XPATH, "/html/body/div[2]")
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class FondationFrance(Scraping):
    def __init__(self):
        super().__init__()
        self.url = "https://www.fondationdefrance.org/fr/"

    def click_cookies(self):
        self.driver.get(self.url)
        sleep(2)
        bouton_xpath_cookie = '//*[@id="onetrust-accept-btn-handler"]'
        click_cookie = self.driver.find_element(By.XPATH, bouton_xpath_cookie).click()

    def scrape_text(self):
        try:
            self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/header/div/div/div/div[2]/div/nav/ul/li[2]",
            ).click()
            texte = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/section[3]/div/main/div/div[2]/div/section[3]/div/div/div/div/div/div/div/div",
            )
            clean_text = re.sub(r"^\s+", "", texte.text)

            self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/header/div/div/div/div[2]/div/nav/ul/li[3]",
            ).click()
            texte = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/section[3]/div/main/div/div[2]/div/section[1]/div[2]/div/div[1]/div/div/div/div/div",
            )
            clean_text += "\n" + re.sub(r"^\s+", "", texte.text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print(clean_text)
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Bougies(Scraping):
    def __init__(self):
        super().__init__()
        self.url = "https://www.bougies-denis.com/fondation-denis-fils/"

    def click_cookies(self):
        self.driver.get(self.url)
        bouton_xpath_cookie = (
            '//*[@id="moove_gdpr_cookie_info_bar"]/div/div/div[2]/button[1]'
        )
        sleep(3)
        click_cookie = self.driver.find_element(By.XPATH, bouton_xpath_cookie).click()

    def scrape_text(self):
        try:
            self.driver.get(self.url)
            sleep(2)

            new_url = (
                self.driver.find_element(By.ID, "menu-item-294")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)
            sleep(2)

            texte = self.driver.find_element(By.XPATH, "/html/body/section")
            clean_text = re.sub(r"^\s+", "", texte.text)

            new_url = (
                self.driver.find_element(By.ID, "menu-item-1530")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)
            sleep(2)

            texte = self.driver.find_element(By.XPATH, "/html/body/section/div[1]")
            clean_text += "\n" + re.sub(r"^\s+", "", texte.text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print(clean_text)
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Lucq(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationdefrance.org/fr/annuaire-des-fondations/fondation-du-lucq"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="sp-component"]/div/div[2]/div[1]'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Patrimoine(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-patrimoine.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)

            while True:
                try:
                    wait = WebDriverWait(
                        self.driver, 10
                    )  # Réduisez le temps d'attente si nécessaire
                    cookie_button = wait.until(
                        EC.element_to_be_clickable(
                            (By.ID, "CybotCookiebotDialogBodyButtonAccept")
                        )
                    )
                    cookie_button.click()
                    sleep(2)
                except:

                    break
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[3]/div/div'
            ).text
            new_url = "https://www.fondation-patrimoine.org/soumettre-un-projet/obtenir-une-aide-financiere"
            self.driver.get(new_url)
            texte += "\n" + self.driver.find_element(By.XPATH, '//*[@id="__next"]').text
            clean_text = re.sub(r"^\s+", "", texte)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Ecotone(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.ecotone.bio/fr/notre-fondation"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "axeptio_btn_acceptAll"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.ID, "post-2012")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Eiffage(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = (
            "https://www.eiffage.com/groupe/presentation-de-la-fondation-eiffage"
        )

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)

            while True:
                try:

                    self.driver.execute_script(
                        "window.scrollBy(0, 100);"
                    )  # Vous pouvez ajuster le défilement en fonction de vos besoins

                    wait = WebDriverWait(self.driver, 10)
                    cookie_button = wait.until(
                        EC.element_to_be_clickable(
                            (By.ID, "onetrust-accept-btn-handler")
                        )
                    )
                    cookie_button.click()
                    sleep(2)
                except:

                    break
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main')
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Ekibio(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.ekibio.fr/la-fondation"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 20)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)

            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="header"]/div/div/div/div[3]/div/nav/ul/li[2]/div/div/div/div/div[2]/ul/li[1]',
            ).find_element(By.TAG_NAME, "a")
            link = about.get_attribute("href")
            sleep(2)

            self.driver.get(link)
            sleep(2)

            self.driver.execute_script("window.scrollBy(0, 8000);")
            sleep(2)

            texte = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[1]")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Enovos(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-enovos.lu/fr/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 15)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "ppms_cm_agree-to-all"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(By.ID, "menu-item-75").find_element(
                By.TAG_NAME, "a"
            )
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(
                By.XPATH, "/html/body/section/div/div[2]/div[1]"
            )
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class GeorgesTruffaut(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-georges-truffaut.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 20)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "cn-accept-cookie"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="page"]/div[1]/section[1]/div/div/div/section[2]/div/div[2]/div/div/div/div/nav/ul/li[1]/ul/li[1]',
            ).find_element(By.TAG_NAME, "a")
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(By.ID, "content")
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Grdf(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationgrdf.fr"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="js-modal-page"]/header/div[1]/nav/div[2]/ul/li[1]/ul',
            ).find_elements(By.TAG_NAME, "a")
            if len(about) >= 2:
                second_a = about[1]
                link = second_a.get_attribute("href")
                sleep(2)
                self.driver.get(link)
                texte = self.driver.find_element(By.ID, "content")
                sleep(1)
                clean_text = re.sub(r"^\s+", "", texte.text)
                print(clean_text)

                df.at[self.cpt_site, "Texte"] = clean_text

                print("\n")
                print("*" * 60)
                sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Ldlc(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-groupe-ldlc.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 20)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]',
                    )
                )
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)

            about = self.driver.find_element(By.ID, "menu-item-885").find_element(
                By.TAG_NAME, "a"
            )
            link = about.get_attribute("href")
            self.driver.get(link)
            sleep(2)

            self.driver.execute_script("window.scrollBy(0, 6000);")
            sleep(2)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="post-849"]/div/div/div/div[3]'
            )
            clean_text1 = re.sub(r"^\s+", "", texte.text)

            sleep(1)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="post-849"]/div/div/div/div[5]'
            )
            clean_text2 = re.sub(r"^\s+", "", texte.text)
            clean_text = clean_text1 + clean_text2
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class GroupePvcp(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.groupepvcp.com/engagement/notre-fondation/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 20)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(By.ID, "menu-item-7502").find_element(
                By.TAG_NAME, "a"
            )
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(By.ID, "main-content")
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class EntrepriseHermes(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationdentreprisehermes.org/fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 20)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="navigation"]/div[1]/nav/ul/li[1]'
            ).find_element(By.TAG_NAME, "a")
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(By.TAG_NAME, "p")
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Humus(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-humus.com"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="menu"]/li[2]'
            ).find_element(By.TAG_NAME, "a")
            link = about.get_attribute("href")
            sleep(2)
            self.driver.get(link)
            texte = self.driver.find_element(By.ID, "content")
            sleep(1)
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)

            df.at[self.cpt_site, "Texte"] = clean_text

            print("\n")
            print("*" * 60)
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class AubertDuval(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationaubertduval.org/"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            # Récupérons le descriptif de la fondation
            self.driver.get(self.site_url)
            new_url = (
                self.driver.find_element(By.ID, "menu-item-194")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )

            self.driver.get(new_url)
            a_propos = self.driver.find_element(
                By.XPATH, "//*[@id='page-content']/div[2]"
            )
            clean_text = re.sub(r"^\s+", "", a_propos.text)
            sleep(2)

            # Récupérons le descriptif de l'appel à projet
            actions = ActionChains(self.driver)
            actions.move_to_element(
                self.driver.find_element(By.ID, "menu-item-195")
            ).perform()  # Survolez l'élément principal du menu

            new_url = (
                self.driver.find_element(By.ID, "menu-item-196")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)

            autre_propos = self.driver.find_element(
                By.XPATH, "//*[@id='page-content']/div[2]"
            )
            clean_text += "\n" + re.sub(r"^\s+", "", autre_propos.text)

            # Récupérons les contacts
            new_url = (
                self.driver.find_element(By.ID, "menu-item-207")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)

            contact_propos = self.driver.find_element(
                By.XPATH, '//*[@id="contact-content"]/div[2]/div/div[1]/div[1]'
            )
            clean_text += "\n" + re.sub(r"^\s+", "", contact_propos.text)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class JulienneDumeste(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationjuliennedumeste.fr/"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            # Ouvrir une page web
            self.driver.get(self.site_url)

            # Attendre que l'élément soit présent et visible
            new_url = (
                WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((By.ID, "menu-item-83")))
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )

            # Accéder à la nouvelle URL
            self.driver.get(new_url)

            # Récupérer le texte de l'élément
            about = self.driver.find_element(
                By.XPATH, "/html/body/div[3]/div/section/div"
            )

            clean_text = re.sub(r"^\s+", "", about.text)
            sleep(2)

            # Information association
            bouton_asso = self.driver.find_element(By.ID, "menu-item-85").click()

            info_asso = self.driver.find_element(
                By.XPATH, "/html/body/div[3]/div/section"
            )
            contact = self.driver.find_element(By.ID, "footersocial")

            clean_text += re.sub(r"^\s+", "", info_asso.text)
            clean_text += re.sub(r"^\s+", "", contact.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class LeaNature(Scraping):

    # Créons les boutons pour naviguer entre les pages
    COOKIE_BUTTON_XPATH = (
        '//*[@id="moove_gdpr_cookie_info_bar"]/div/div/div[2]/button[1]'
    )
    ABOUT_XPATH = "/html/body/section[1]/div/div/div[2]"
    PROJECT_BUTTON_XPATH = "/html/body/section[2]/div[1]/section/div/div[12]/div[1]"
    PROJECT_TEXT_XPATH = "/html/body/section[2]/div"

    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-mecenat-leanature.org/qui-sommes-nous/notre-organisation/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button = self.driver.find_element(By.XPATH, self.COOKIE_BUTTON_XPATH)
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            # Récupérer le descriptif de la fondation
            about = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.ABOUT_XPATH))
            )
            clean_text = re.sub(r"^\s+", "", about.text)

            # Récupérer le descriptif de l'offre
            self.driver.find_element(By.XPATH, self.PROJECT_BUTTON_XPATH).click()
            project_text = self.driver.find_element(By.XPATH, self.PROJECT_TEXT_XPATH)
            clean_text += "\n" + re.sub(r"^\s+", "", project_text.text)

            # Récupérer les contacts
            contact_links = [
                self.driver.find_element(By.ID, "menu-item-20")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href"),
                self.driver.find_element(By.ID, "menu-item-4506")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href"),
            ]
            contact_text = "\n".join(contact_links)
            clean_text += "\n" + re.sub(r"^\s+", "", contact_text)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Lemarchand(Scraping):
    COOKIE_BUTTON_XPATH = '//*[@id="cookie-accept-btn"]'
    ABOUT_LINK_XPATH = '//*[@id="header-main-menu"]/ul/li[2]/a'
    PROJECT_LINK_XPATH = '//*[@id="page-footer"]/div[2]/div/section[2]/nav/ul/li[5]/a'
    CONTACT_LINK_XPATH = '//*[@id="header-main-menu"]/ul/li[3]'

    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondationlemarchand.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button = self.driver.find_element(By.XPATH, self.COOKIE_BUTTON_XPATH)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            # Récupérer le texte de la fondation
            self.driver.get(self.site_url)
            about_link = self.driver.find_element(By.XPATH, self.ABOUT_LINK_XPATH)
            new_url = about_link.get_attribute("href")
            self.driver.get(new_url)
            about_text = self.driver.find_element(By.XPATH, '//*[@id="editorial"]').text
            causes_text = self.driver.find_element(By.XPATH, '//*[@id="causes"]').text

            # Récupérer le texte du projet
            project_link = self.driver.find_element(By.XPATH, self.PROJECT_LINK_XPATH)
            new_url = project_link.get_attribute("href")
            self.driver.get(new_url)
            project_text = self.driver.find_element(
                By.XPATH, '//*[@id="proposer-projet"]/div[2]'
            ).text

            # Récupérer les contacts
            contact_link = self.driver.find_element(
                By.XPATH, self.CONTACT_LINK_XPATH
            ).click()
            link_candidate = (
                self.driver.find_element(By.XPATH, '//*[@id="contact-form"]/p')
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            contact_text = self.driver.find_element(
                By.XPATH, '//*[@id="contact-form"]/p'
            ).text

            clean_text = "\n".join(
                [about_text, causes_text, project_text, contact_text, link_candidate]
            )
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class M6(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.groupem6.fr/engagements/la-fondation/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_Xpath = (
                '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]'
            )
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_Xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            # Récupérons la description de la fondation
            about = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[4]/div[1]/div/p[1]'
            )
            clean_about = re.sub(r"^\s+", "", about.text)

            sleep(2)
            # Récupérons la description du projet
            text_project = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[8]/div'
            )
            clean_project = re.sub(r"^\s+", "", text_project.text)

            link_project = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[8]/div/div[5]'
            ).get_attribute("href")
            sleep(2)

            # Récupérons les contacts menu-item-493
            contact_button = self.driver.find_element(By.ID, "menu-item-493").click()

            contact_url = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[2]/div/div[3]/div[2]/a'
            ).get_attribute("href")
            contact_text = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/div[2]/div/div[3]/div[2]/a'
            )
            clean_contact = re.sub(r"^\s+", "", contact_text.text)

            sleep(2)
            clean_text = "\n".join(
                [clean_about, clean_project, clean_contact, contact_url]
            )
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Macif(Scraping):

    BUTTON_FONDATION_XPATH = '//*[@id="skrollr-body"]/main/section[1]/div/div/div/div[1]/nav/ul/li[1]/a'  # On va utiliser le bouton là plusieurs fois
    CONTENU_FONDATION_XPATH = (
        '//*[@id="skrollr-body"]/main/section[2]/div/div/div[2]/div'
    )
    FINANCEMENT_BUTTON_XPATH = '//*[@id="skrollr-body"]/main/section[1]/div/div/div/div[1]/nav/ul/li[1]/ul/li[5]/a'
    PROJET_BUTTON_XPATH = '//*[@id="skrollr-body"]/main/section[1]/div/div/div/div[1]/nav/ul/li[1]/ul/li[6]'

    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-macif.org/page/appel-a-projet-idf"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            actions = ActionChains(self.driver)

            # Récupérer les infos de la fondations
            self.driver.find_element(By.XPATH, self.BUTTON_FONDATION_XPATH).click()
            about = self.driver.find_element(
                By.XPATH, self.CONTENU_FONDATION_XPATH
            ).text
            clean_text = re.sub(r"^\s+", "", about)

            # Récupérer les infos de financement
            actions.context_click(
                self.driver.find_element(By.XPATH, self.BUTTON_FONDATION_XPATH)
            ).perform()  # CLIQUE DROIT SUR l'élément
            self.driver.find_element(By.XPATH, self.FINANCEMENT_BUTTON_XPATH).click()
            finacement_text = self.driver.find_element(
                By.XPATH, '//*[@id="skrollr-body"]/main/section[2]/div/div'
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", finacement_text)

            # Récupérer les infos  des projets
            actions.context_click(
                self.driver.find_element(By.XPATH, self.BUTTON_FONDATION_XPATH)
            ).perform()
            self.driver.find_element(By.XPATH, self.PROJET_BUTTON_XPATH).click()
            projet_text = self.driver.find_element(
                By.XPATH, '//*[@id="skrollr-body"]/main/section[2]'
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", projet_text)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class MaisonDuMonde(Scraping):

    BUTTON_FONDATION_ID = "menu-item-156"
    BUTTON_PROJET_ID = "menu-item-10817"
    TEXT_FONDATION_XPATH = '//*[@id="main"]'
    TEXT_PROJET_XPATH = '//*[@id="main"]'

    def __init__(self):
        super().__init__()
        self.site_url = "https://foundation.maisonsdumonde.com"

    def click_cookies(self):
        pass  # pas de cookies

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            self.driver.find_element(By.ID, self.BUTTON_FONDATION_ID).click()

            # Descriptif de la fondation
            text_fondation = self.driver.find_element(
                By.XPATH, self.TEXT_FONDATION_XPATH
            ).text
            clean_text = re.sub(
                r"^\s+", "", text_fondation
            )  # Suppression des espaces en début de ligne

            self.driver.find_element(By.ID, self.BUTTON_PROJET_ID).click()
            # Descriptif du projet
            text_projet = self.driver.find_element(
                By.XPATH, self.TEXT_PROJET_XPATH
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", text_projet)

            # CONTACT
            # il faut remplir un formulaire sur leur page pour les contacter
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Michelin(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation.michelin.com/la-fondation/qui-sommes-nous"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            cookie_button = self.driver.find_element(By.ID, "tarteaucitronPersonalize2")
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            # Description fondation
            a_propos_fondation = self.driver.find_element(
                By.XPATH,
                '//*[@id="fl-post-1147"]/div/div/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div',
            )
            clean_text = re.sub(r"^\s+", "", a_propos_fondation.text)

            # Description projet
            self.driver.find_element(By.ID, "menu-item-2353").click()
            a_propos_projet = self.driver.find_element(
                By.XPATH,
                '//*[@id="fl-post-2322"]/div/div/div[2]/div/div/div/div[2]/div',
            ).text
            clean_text += "\n" + re.sub(
                r"^\s+", "", a_propos_projet
            )  # Critères d'éligibilité sous forme de pdf

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Children(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://777children.fr"

    def click_cookies(self):
        pass  # pas de cookies

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="menu-1-1d4584a0"]/li[1]'
            ).find_element(By.TAG_NAME, "a")
            new_url = texte.get_attribute("href")

            self.driver.get(new_url)
            # Descriptif fondation
            a_propos = self.driver.find_element(By.XPATH, "/html/body/div")
            clean_text = re.sub(r"^\s+", "", a_propos.text)

            # Descriptif  Projet
            self.driver.find_element(
                By.XPATH,
                "/html/body/header/section[1]/div/div/div/div/div/div/a/span/span[2]",
            ).click()
            a_propos_projet = self.driver.find_element(
                By.XPATH, "/html/body/div/section[2]/div/div/div/div[2]/div/div/ul"
            ).text
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos_projet)

            # Contact (la demande se fait via un formulaire)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class OAK(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://oakfnd.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = (
                '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]'
            )
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            self.driver.find_element(By.XPATH, '//*[@id="menu-item-15884"]').click()

            new_url = self.driver.find_element(
                By.XPATH, '//*[@id="menu-item-40018"]/a'
            ).get_attribute("href")
            self.driver.get(new_url)

            # Descriptif fondation
            a_propos_fondation = self.driver.find_element(
                By.XPATH, '//*[@id="post-56"]'
            ).text
            clean_text = re.sub(r"^\s+", "", a_propos_fondation)

            # Contact
            self.driver.find_element(By.XPATH, '//*[@id="menu-item-13668"]').click()
            about_contact = self.driver.find_element(
                By.XPATH, '//*[@id="post-88"]/div[4]/div[3]/p'
            ).text
            url_contact = (
                self.driver.find_element(By.XPATH, '//*[@id="post-88"]/div[4]/div[3]/p')
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            clean_text += "\n" + re.sub(r"^\s+", "", about_contact)
            clean_text += "\n" + re.sub(r"^\s+", "", url_contact)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Orcom(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation.orcom.fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = '//*[@id="cookie_action_close_header"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            self.driver.find_element(
                By.ID, "chbx"
            ).click()  # Clicker sur le bouton burger

            new_url = (
                self.driver.find_element(By.ID, "menu-item-76")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )

            self.driver.get(new_url)
            # Description Fondation
            a_propos = self.driver.find_element(By.XPATH, "/html/body/div[1]/div")
            clean_text = re.sub(r"^\s+", "", a_propos.text)

            # PROJET

            new_url = (
                self.driver.find_element(By.ID, "menu-item-81")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)
            # CRITERES ET PROCESSUS
            a_propos = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]"
            )
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos.text)

            new_url = (
                self.driver.find_element(By.ID, "menu-item-80")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)
            # APPEL A PROJET
            a_propos = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]"
            )
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos.text)

            new_url = (
                self.driver.find_element(By.ID, "menu-item-79")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)
            # DEPOSER UN DOSSIER
            a_propos = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[1]/section[2]/div/div[1]/div"
            )
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos.text)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Palatine(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.palatine.fr/votre-banque/nos-engagements/partenariats-mecenats/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = '//*[@id="consent_prompt_submit"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="bpce-menu-top"]/ul/li[2]/button'
            ).click()
            texte2 = self.driver.find_element(
                By.XPATH, '//*[@id="need-0"]/div/p[1]'
            ).click()
            texte3 = self.driver.find_element(
                By.XPATH,
                '//*[@id="offer-block_34f6e6e2ae6b19d8ca2afbda8b517812"]/div/div/div[2]/div/div/h2',
            ).find_element(By.TAG_NAME, "a")
            new_url = texte3.get_attribute("href")

            self.driver.get(new_url)

            a_propos = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/section[2]/div/div/div/div[2]/div'
            ).text
            a_propos += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/section[3]/div/div/div/div[2]/div'
                ).text
            )
            a_propos += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="h-le-fruit-d-une-histoire-europeenne"]'
                ).text
            )
            a_propos += (
                "\n"
                + self.driver.find_element(
                    By.XPATH, '//*[@id="main"]/section[5]/div/div/div/div[2]/div'
                ).text
            )
            clean_text = re.sub(r"^\s+", "", a_propos)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Patagonia(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://eu.patagonia.com/fr/fr/how-we-fund/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            a_propos = self.driver.find_element(
                By.XPATH, "/html/body/main/section/div[2]/section/div[2]/div"
            )
            clean_text = re.sub(r"^\s+", "", a_propos.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Puressentiel(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fr.puressentiel.com/pages/fondation-puressentiel"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)

            cookie_button_xpath = '//*[@id="shopify-pc__banner__btn-accept"]'
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)

            a_propos = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]")
            clean_text = re.sub(r"^\s+", "", a_propos.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Raja(Scraping):

    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-raja-marcovici.com"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button_xpath = "cookie_ok"
            cookie_button = self.driver.find_element(By.XPATH, cookie_button_xpath)
            cookie_button.click()

            hide_button_xpath = '//*[@id="cookie_hide"]'
            hide_button = self.driver.find_element(By.XPATH, hide_button_xpath)
            hide_button.click()
            sleep(2)
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            actions = ActionChains(self.driver)
            actions.context_click(
                self.driver.find_element(By.XPATH, '//*[@id="menu-item-210"]')
            ).perform()

            self.driver.find_element(By.ID, "menu-item-45").click()

            a_propos = self.driver.find_element(By.XPATH, "/html/body/section[1]")
            clean_text = re.sub(r"^\s+", "", a_propos.text)

            # PROJET
            new_url = (
                self.driver.find_element(
                    By.XPATH, '//*[@id="header"]/div/div[3]/div/div[2]'
                )
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )
            self.driver.get(new_url)

            # Descriptif projet
            a_propos_projet = self.driver.find_element(
                By.XPATH, "/html/body/section[1]/div"
            )
            clean_text += "\n" + re.sub(r"^\s+", "", a_propos_projet.text)

            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)

        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class RATP(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://ratpgroup.com/fr/le-groupe-ratp/fondation-groupe-ratp/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            cookie_button = self.driver.find_element(By.ID, "popin_tc_privacy_button_3")
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.XPATH, '//*[@id="site-content"]/div')
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class RTE(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-rte.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()  # Pause pour laisser le temps à la page de réagir après le clic
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/ul'
            ).find_element(By.TAG_NAME, "a")
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="block-fondation-content"]/div/div/div/div[3]/div'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Rexel(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.rexelfoundation.com/fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="block-menu-menu-refonte-main-menu"]/ul/li[1]/div/ul'
            ).find_element(By.TAG_NAME, "a")
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="node-544"]/div[2]/div[2]'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class SaintGobain(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation.saint-gobain.com"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, '//*[@id="fast-cmp-home"]/nav/span[3]/button')
                )
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="block-fsg-content"]/div/article/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/p[3]/a',
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="block-fsg-content"]/div/article/div'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class SchneiderElectric(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.se.com/fr/fr/about-us/sustainability/foundation/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "accept-recommended-btn-handler"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_elements(By.XPATH, "/html/body/main/div[*]")
            for e in texte:
                clean_text = re.sub(r"^\s+", "", e.text)
                print(clean_text)
                df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class Setec(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondationsetec.org"

    def click_cookies(self):
        pass

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_elements(By.XPATH, '//*[@class="bref"]')
            for e in texte:
                clean_text = re.sub(r"^\s+", "", e.text)
                print(clean_text)
                df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class SocieteGenerale(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation.societegenerale.com/fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="block-sg-fondation-main-menu"]/ul/li[1]'
            ).click()
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="block-sg-fondation-content"]/article/div/div'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class TerreSolidaire(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondation-terresolidaire.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            sleep(2)
            self.driver.find_element(
                By.XPATH, '//*[@id="tarteaucitronPersonalize2"]'
            ).click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            about = self.driver.find_element(
                By.XPATH, '//*[@id="content"]/article/div/div[1]/div'
            ).find_element(By.TAG_NAME, "a")
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(By.ID, "content")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class UEM(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-uem.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
                )
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="post-9"]/div[1]/div/div/div'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class VinciPourLaCite(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.fondation-vinci.com"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH, '//*[@id="menu-menu-principal"]/li[1]/div/ul/li[1]'
            ).find_element(By.TAG_NAME, "a")
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(By.ID, "maincontent")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class WattsForChange(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.wattforchange.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(By.ID, "menu-item-182").find_element(
                By.TAG_NAME, "a"
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(By.XPATH, '//*[@id="post-7"]/div[*]')
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class JeanBaudelet(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://fondsjeanbaudelet.fr"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(By.ID, "menu-item-557").find_element(
                By.TAG_NAME, "a"
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(
                By.XPATH, '//*[@id="Content"]/div/div/div/div[1]'
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class DotationTerreFils(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://terreetfils.org/ecosysteme/fonds-de-dotation/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class EntreprendreETPLUS(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://www.entreprendreetplus.org"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="top"]/div[3]/div[1]/div/a[1]')
                )
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(By.ID, "menu-item-1514").find_element(
                By.TAG_NAME, "a"
            )
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(By.ID, "wrap_all")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class UnEspritDeFamille(Scraping):
    def __init__(self):
        super().__init__()
        self.site_url = "https://unespritdefamille.org/membre/le-chant-des-etoiles/"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="moove_gdpr_cookie_info_bar"]/div/div/div[2]/button',
                    )
                )
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            texte = self.driver.find_element(By.ID, "et-main-area")
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


class KloraneBotanical(Scraping):

    def __init__(self):
        super().__init__()
        self.site_url = "https://www.kloranebotanical.foundation"

    def click_cookies(self):
        try:
            self.driver.get(self.site_url)
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erreur lors du clic sur les cookies : {e}")

    def scrape_text(self):
        try:
            self.driver.get(self.site_url)
            about = self.driver.find_element(
                By.XPATH,
                '//*[@id="block-navigationprincipale"]/div/div/ul/li[1]/div/ul/li[1]',
            ).find_element(By.TAG_NAME, "a")
            new_url = about.get_attribute("href")
            self.driver.get(new_url)
            texte = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/main/div/div/article/div/div[3]/div[2]"
            )
            clean_text = re.sub(r"^\s+", "", texte.text)
            print(clean_text)
            df.at[self.cpt_site, "Texte"] = clean_text
            print("\n")
            print("*" * 60)
        except ElementNotInteractableException:
            print("L'élément n'est pas interactable.")
        except Exception as e:
            print(f"Erreur lors du scraping du texte : {e}")


classes_to_execute = [
    PourLaPlanete,
    AkuoFoundation,
    ConcoursGreenLink,
    Danone,
    FapeEngie,
    FFB,
    Abalone,
    AccorHotel,
    AG2RLaMondiale,
    AirLiquide,
    Alstom,
    AmaryServir,
    Artelia,
    Autonomia,
    Bardon,
    Batigère,
    Baudoux,
    Biocoop,
    BNPParibas,
    LouisBonduelle,
    Brageac,
    Carasso,
    Caritas,
    Cassiopee,
    PaysDeFrance,
    FondationFrance,
    Bougies,
    Lucq,
    Patrimoine,
    Ecotone,
    Eiffage,
    Ekibio,
    Enovos,
    GeorgesTruffaut,
    Grdf,
    Ldlc,
    GroupePvcp,
    EntrepriseHermes,
    Humus,
    AubertDuval,
    JulienneDumeste,
    LeaNature,
    Lemarchand,
    M6,
    Macif,
    MaisonDuMonde,
    Michelin,
    Children,
    OAK,
    Orcom,
    Palatine,
    Patagonia,
    Puressentiel,
    Raja,
    RATP,
    Rexel,
    RTE,
    SaintGobain,
    SchneiderElectric,
    Setec,
    SocieteGenerale,
    TerreSolidaire,
    UEM,
    VinciPourLaCite,
    WattsForChange,
    JeanBaudelet,
    DotationTerreFils,
    EntreprendreETPLUS,
    UnEspritDeFamille,
    KloraneBotanical,
]

test_Execution = [TerreSolidaire]


def execute_classes(classes):
    for class_type in classes:
        instance = class_type()
        instance.click_cookies()
        instance.scrape_text()
        instance.close_browser()


if __name__ == "__main__":
    execute_classes(classes_to_execute)
    # execute_classes(test_Execution)

    df.to_excel(r"Fondations.xlsx",index=False,)

## Partie 2 : Affinement de la base de données à l'aide du llm et du Excel modèle
