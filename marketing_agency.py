from crewai import Crew
from dotenv import load_dotenv

load_dotenv()

print(' ------- WELCOME TO THE RICHAI MARKETING AGENCY ------- ')
print(' ------------------------------------------------------ ')
company_name = input("What is the name of your company?\n")
company_details = input("What can you tell-me about this company?\n")

# --- IMPORTAR AGENTES ---
from agents import market_analyst_agent, director_agent, content_creator_agent, marketing_strategist_agent, photographer_agent


# --- IMPORTAR AS TAREFAS ---
from tasks import MarketingAnalysisTasks
tasks = MarketingAnalysisTasks()
company_analysis = tasks.company_analysis(market_analyst_agent, company_name, company_details)
market_analysis = tasks.competitor_analysis(market_analyst_agent, company_name, company_details)
campaing_development = tasks.campaign_development(marketing_strategist_agent, company_name, company_details)
write_copy = tasks.instagram_ad_copy(content_creator_agent)

# --- MONTAR A EQUIPE DE COPY ---
campaign_crew = Crew(
    agents=[
        market_analyst_agent,
        marketing_strategist_agent,
        content_creator_agent
    ],
    tasks=[
        company_analysis,
        market_analysis,
        campaing_development,
        write_copy
    ],
    verbose=True
)
campaign = campaign_crew.kickoff()

# --- MONTAR A EQUIPE DE FOTOGRAFIA ---

take_photograph = tasks.take_photograph_task(photographer_agent, campaign, company_name, company_details)
review_photograph = tasks.review_photo(director_agent, company_name, company_details)

image_crew = Crew(
    agents=[
        photographer_agent,
        director_agent
    ],
    tasks=[
        take_photograph,
        review_photograph
    ],
    verbose=True
)

# --- TRABALHAR! ---
images = image_crew.kickoff()

# --- APRESENTAR AS CAMPANHAS ---
print("\n\n ------------------------ \n")
print("Estas foram as campanhas que preparamos para sua empresa: ")
print("\n ------------------------ \n")
print("Aqui está a campanha: \n")
print(campaign)
print("\n\n ------------------------ \n")
print("Aqui estão as imagens (Descrições para o DALL-E/Midjourney): \n")
print(images)