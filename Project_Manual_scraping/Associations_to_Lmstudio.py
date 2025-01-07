import pandas as pd
from openai import OpenAI

## 1 Création du dataframe contenant les informations sur les associations.


def create_info_asso():

    data = pd.DataFrame()

    data["Associations"] = [
        "LeBurgerSuspendu",
        "AmiTomaké",
        "ClimateProtectors",
        "Le Next Level",
        "Rêv'Elle Toi",
    ]

    data["Textes"] = [
        "Permettre aux étudiants en précarité de manger un menu grâce à notre réseau de restaurants partenaires",
        "Notre mission est l’inclusion sociale par la pratique d’activités physiques, de bien-être et de loisirs des personnes avec des troubles du neurodéveloppement à savoir : les troubles de la communication, les troubles du spectre de l’autisme, les troubles spécifiques des apprentissages, les troubles moteurs, le déficit de l’attention/hyperactivité… et ainsi permettre à chaque enfant d’avoir accès aux loisirs au même titre que les autres enfants. Par notre action, nous soutenons les parents d’enfants extraordinaires qui ont besoin de ces moments de répit pour maintenir leur propre bien-être, pour préserver l’harmonie au sein de la famille, pour améliorer la qualité des soins aux enfants, et pour éviter l’épuisement parental. Accorder du temps de répit à ces parents est une manière de reconnaître et de soutenir leur dévouement inestimable. C’est également un investissement dans la santé et le bien-être de la famille dans son ensemble.",
        "« Climate Protectors » est une communauté intergénérationnelle de pionniers exceptionnels. Inspirer de jeunes acteurs du changement et des parents impressionnants en position d'influence, co-créant une nouvelle réalité avec et pour leurs enfants. Pour révéler le potentiel des parents en position d'influence pour avoir un impact transformateur, « Climate Protector » conçoit des approches révolutionnaires et organise du contenu et des outils uniques avec des experts de renommée internationale en matière d'action et de solutions climatiques à grande échelle. Un atout inestimable et inexploité est le petit nombre de personnes occupant des postes de direction, dotées de talents extraordinaires, de personnalités et d'états d'esprit uniques, de réseaux, de compétences, d'expertise, de leadership, d'influence, de ressources et de pouvoir qui les placent dans une position tout à fait unique, d'où leurs décisions et leurs actions peuvent avoir un impact à grande échelle et des répercussions majeures pour façonner nos systèmes et nos sociétés vers un modèle régénérateur et durable. Les 0,1 % de personnes ayant une influence exceptionnelle ont le potentiel d’être les plus grands acteurs du changement dans la crise environnementale. Parmi ceux qui appartiennent aux 0,1 % et qui s’engagent sur une nouvelle voie vers la durabilité, la grande majorité a été profondément façonnée par la prise de conscience de l’urgence d’agir pour protéger et protéger leurs enfants d’un effondrement du système induit par le changement climatique. L'histoire est toujours écrite par des pionniers. Les personnes en position de grande influence qui exploitent leurs talents uniques pour lutter contre le changement climatique peuvent devenir les leaders les plus influents dans la transition et devenir de nouveaux modèles et créateurs de tendances pour l'ensemble de la société, établissant une nouvelle norme sociale que tous pourront adopter et imiter.",
        "Le Next Level a pour mission de co-produire, accompagner et participer à des démarches favorisant la justice, l’équité, et le respect de la dignité des personnes, par tout moyen nécessaire et disponible. Son action se décline en 3 axes : formation, accompagnement stratégique, et animation d’une communauté de valeurs souhaitant agir ensemble, en complémentarité, au-delà de leur seul secteur d’activité. Dans cette communauté, tout le monde forme tout le monde : de l’équipe salariée aux invité·es de marque venu·es d’ailleurs, en passant par le cercle des pros, les membres des collectifs ou les partenaires, chacun·e partage ses connaissances, son expérience, ses compétences et ses ressources au service du collectif.",
        "Aider les femmes à remettre ou à trouver de l’harmonie sur le chemin de leur vie. Le but premier est d’accompagner les femmes à se révéler à elles-mêmes d’abord, puis au monde ensuite",
    ]

    data.to_excel(r"Associations.xlsx",index=False,)

    return data


info_associations = create_info_asso()

## 2 - Extraction des mots clés de la colonne Texte


class LocalOpenAI:
    def __init__(self):
        self.client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    def extraction_informations_cles(self, dataframe):
        user_message = f'Réponds en francais : Dans le texte : {dataframe["Textes"]}, donne moi de facon très claire, concise et sans faire d introduction les informations clés qui caractérise le mieux l association décrite par ce texte.'

        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant spécialisé dans la recherche d'aide au financement d'associations très performant et expérimenté. Tu es également extrêmement concis et précis dans tes réponses",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content


local_openai = LocalOpenAI()

info_associations["Informations clés"] = info_associations.apply(
    local_openai.extraction_informations_cles, axis=1
)

## 3 - Récupérer le dataframe final

info_associations.to_excel(r"Associations_Lmstudio.xlsx",index=False)
