import pandas as pd
from openai import OpenAI

## 1- Appel de la base de donnée déjà faite Via Fondations_to_scraper.py

fondations = pd.read_csv(
    r"Fondations.csv"
)

fondations = fondations.drop(columns="Unnamed: 0")

##Supressions des lignes vides
#   fondations = fondations.dropna()

print(fondations)


## 2- Création des fonctions d'extractions avec l'aide de lmstudio


class LocalOpenAI:
    def __init__(self):
        self.client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    def extraction_informations_cles(self, dataframe):
        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, extrait moi sans faire d introduction les informations clés qui pourraient permettre à une association de savoir si elle pourrait postuler à l appel d offre que mettra en place cette fondation.'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_date_butoire(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné une date butoire pour le dépot d un dossier. Si Oui, donne la date butoire, sinon écrit "Pas de date butoire" sans rien ajouter de plus ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_type_de_financeur(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Parmi les types de financeurs suivants : ["Fondation d entreprise", "Fonds de dotation", "Fond public", "Institution publique", "Fondation familiale"] laquelle correspond le plus à la fondation présentée dans le texte, répond en ne donnant que l un des possibles types fournis'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_nom_appel(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné le nom d appel mis en place par la fondation ? Si Oui, donne le sans rien ajouter de plus, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_champs_intervention(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Retourne moi sous forme de liste, sans rien ajouter de plus, les 3 principaux champs d interventions principaux de la fondation'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_criteres_cles(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné des conditions / critères clés que l association désireuse de candidater doit vérifier ? Si Oui, donne les sans rien ajouter de plus, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_parrainage(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné l obligation d avoir un parrain ou une marraine pour déposer un dossier ? Si Oui, écrit "Oui" sans rien ajouter de plus, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_don(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné le Don / subvention potentiel(le) ou moyen(ne) que peut fournir la fondation pour un projet donné ? Si Oui, donne le sans rien ajouter de plus, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    ## Contact

    def extraction_tel(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné le numéro de téléphone de la fondation ? Si Oui, donne le sans rien ajouter de plus, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_mail(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné le mail de la fondation ? Si Oui, donne le, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    ## Processus

    def extraction_processus(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné un processus de dépot et de traitement de dossier ? Si Oui, Résume le plus clairement et brièvement possible, sinon écrit "Non metionné" sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_janvier(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Janvier ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_fevrier(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Février ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_mars(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Mars ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_avril(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Avril ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_mai(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Mai ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_juin(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Juin ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_juillet(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Juillet ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_aout(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Août ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_septembre(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Septembre ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_octobre(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Octobre ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_novembre(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Novembre ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_décembre(self, dataframe):

        user_message = f'Réponds en francais uniquement et qu avec oui ou non : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature en Décembre ?'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_libre(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné qu une association peut déposer un dossier de candidature à tout moment ? Réponds que par oui ou non sans rien ajouter de plus'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def extraction_mentionné(self, dataframe):

        user_message = f'Réponds en francais uniquement : Dans le texte : {dataframe["Texte"]}, Est-il mentionnné une période dans laquelle une association peut déposer un dossier ? Réponds que par oui ou non sans rien ajouter de plus.'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant francais spécialisé dans la recherche d'aide au financement d'associations très performant, expérimenté et qui ne peut répondre que par 'Oui' ou 'Non' sans rien ajouter de plus. Tu es également extrêmement concis et précis dans tes réponses. Sois le plus strict et précis possible, si l'information demandée n'est pas présente n'hésite pas à répondre 'Non' sans rien ajouter de plus ",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content


## 3- Création des colonnes supplémentaires du dataset

local_openai = LocalOpenAI()

fondations["Informations cles"] = fondations.apply(
    local_openai.extraction_informations_cles, axis=1
)
fondations["Date butoire"] = fondations.apply(
    local_openai.extraction_date_butoire, axis=1
)
fondations["Type de financeur"] = fondations.apply(
    local_openai.extraction_type_de_financeur, axis=1
)
fondations["Nom de l'appel"] = fondations.apply(
    local_openai.extraction_nom_appel, axis=1
)
fondations["Champs d'intervention"] = fondations.apply(
    local_openai.extraction_champs_intervention, axis=1
)
fondations["Criteres cles"] = fondations.apply(
    local_openai.extraction_criteres_cles, axis=1
)
fondations["Parrainage"] = fondations.apply(local_openai.extraction_parrainage, axis=1)
fondations["Don / subvention potentiel(le) ou moyen(ne)"] = fondations.apply(
    local_openai.extraction_don, axis=1
)

fondations["Telephone"] = fondations.apply(local_openai.extraction_tel, axis=1)
fondations["Mail"] = fondations.apply(local_openai.extraction_mail, axis=1)

fondations["Processus"] = fondations.apply(local_openai.extraction_processus, axis=1)
fondations["Janvier"] = fondations.apply(local_openai.extraction_janvier, axis=1)
fondations["Fevrier"] = fondations.apply(local_openai.extraction_fevrier, axis=1)
fondations["Mars"] = fondations.apply(local_openai.extraction_mars, axis=1)
fondations["Avril"] = fondations.apply(local_openai.extraction_avril, axis=1)
fondations["Mai"] = fondations.apply(local_openai.extraction_mai, axis=1)
fondations["Juin"] = fondations.apply(local_openai.extraction_juin, axis=1)
fondations["Juillet"] = fondations.apply(local_openai.extraction_juillet, axis=1)
fondations["Aout"] = fondations.apply(local_openai.extraction_aout, axis=1)
fondations["Septembre"] = fondations.apply(local_openai.extraction_septembre, axis=1)
fondations["Octobre"] = fondations.apply(local_openai.extraction_octobre, axis=1)
fondations["Novembre"] = fondations.apply(local_openai.extraction_novembre, axis=1)
fondations["Decembre"] = fondations.apply(local_openai.extraction_décembre, axis=1)
fondations["Libre"] = fondations.apply(local_openai.extraction_libre, axis=1)
fondations["Non mentionne"] = fondations.apply(
    local_openai.extraction_mentionné, axis=1
)

## 4- Affichage du dataset résultant et exportation

print(fondations)

fondations.to_csv(
    r"Fondations_Lmstudio.csv"
)
