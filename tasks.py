from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def company_analysis(self, agent, company_name, company_details):
		return Task(
			description=dedent(f"""\
			Analyze the given company: {company_name}.
			Extra details provided by the customer: {company_details}.

			Focus on identifying unique features, benefits,
			and the overall narrative presented.

			Your final report should clearly articulate the
			company's key selling points, its market appeal,
			and suggestions for enhancement or positioning.
			Emphasize the aspects that make the company stand out.

			Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
			"""),
			agent=agent,
			expected_output="A detailed report about the company."
		)

	def competitor_analysis(self, agent, company_name, company_details):
		return Task(
			description=dedent(f"""\
			Explore competitor of: {company_name}.
			Extra details provided by the customer: {company_details}.

			Identify the top 3 competitors and analyze their
			strategies, market positioning, and customer perception.

			Your final report MUST include BOTH all context about {company_details}
			and a detailed comparison to whatever competitor they have competitors.
			"""),
			agent=agent,
			expected_output="A report including all context about the company and comparison with competitors."
		)

	def campaign_development(self, agent, company_name, company_details):
		return Task(
			description=dedent(f"""\
			You're creating a targeted marketing campaign for: {company_name}.
			Extra details provided by the customer: {company_details}.

			To start this campaing we will need a strategy and creative content ideas.
			It should be meticulously designed to captivate and engage
			the product's target audience.

			Based on your ideas your co-workers will create the content for the campaign.

			Your final answer MUST be ideas that will resonate with the audience and
			also include ALL context you have about the product and the customer.
			"""),
			agent=agent,
			expected_output="A list of ideas that includes context and is awesome for the audience."
		)

	def instagram_ad_copy(self, agent):
		return Task(
			description=dedent("""\
			Craft an engaging Instagram post copy.
			The copy should be punchy, captivating, concise,
			and aligned with the product marketing strategy.

			Focus on creating a message that resonates with
			the target audience and highlights the product's
			unique selling points.

			Your ad copy must be attention-grabbing and should
			encourage viewers to take action, whether it's
			visiting the website, making a purchase, or learning
			more about the product.

			Your final answer MUST be 3 options for an ad copy for instagram that
			not only informs but also excites and persuades the audience.
			"""),
			agent=agent,
			expected_output="3 options for an ad copy for instagram."
		)

	def take_photograph_task(self, agent, copy, company_name, company_details):
		return Task(
			description=dedent(f"""\
			You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an instagram post
			regarding the product, you have the following copy:
			{copy}

			This is the company you are working with: {company_name}.
			Extra details provided by the customer: {company_details}.

			Imagine what the photo you wanna take describe it in a paragraph.
			Here are some examples for you follow:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product on the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
			"""),
			agent=agent,
			expected_output="3 options of photographs, each with 1 paragraph describing the photograph exactly"
		)

	def review_photo(self, agent, company_name, company_details):
		return Task(
			description=dedent(f"""\
			Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			This is the company you are working with: {company_name}.
			Extra details provided by the customer: {company_details}.

			Here are some examples on how the final photographs should look like:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
			"""),
			agent=agent,
			expected_output="3 reviewd options of photographs, describing exaclty how the photograph is in a very detailed way."
		)