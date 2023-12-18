<template>
  <Navbar />

  <!-- == HERO == -->
  <div
    class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
    <h1 class="text-3xl lg:text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">
      Screen Tastes: The Users vs. Critics Conundrum
    </h1>
    <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain movie
      taste differences between users and critics</h3>
    <div class="flex flex-col items-center mt-auto px-5 py-3">
      <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] mt-3">A project served by the Team
        rADAtouille</span>
      <div class="flex flex-wrap gap-1 items-center justify-center mt-2">
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Antonin Faure</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Baptiste Lecoeur</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Enzo Palmisano</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Jamil Maj</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Mariella Daghfal</span>
      </div>
    </div>
  </div>

  <!-- Main -->
  <main class="grid grid-cols-5 w-full items-center overflow-hidden text-justify">
    <!--
    <div class="cols-1 pl-8">
      <div class="lamp-container">
        <img :src="activeLamp ? '/lamp_right.png' : '/lamp_face.png'" alt="lamp face" class="lamp cursor-pointer"
          @click="toggleLamp" />
        <svg v-show="activeLamp" class="light-aura" width="1000" height="600" viewBox="0 0 500 300"
          preserveAspectRatio="xMidYMin slice">
          <polygon points="350,100 800,100 204,6 197,16" fill="yellow" />
        </svg>
      </div>
    </div>
    -->
    <div class="flex col-span-5 px-10 lg:px-8 lg:col-span-3 lg:col-start-2 flex-col py-8 w-full mx-auto max-w-screen-lg">
      <section id="introduction" class="section">
        <h2 class="text-5xl font-bold mt-5">Introduction</h2>

        <div class="flex flex-col lg:flex-row">
          <div>
            <p class="text-justify mt-4 lg:max-w-screen-md">
              As aspiring chefs, we are eager to learn how to prepare the most exquisite movie
              possible. We are aware that Anton Ego, a renowned critic, will soon be evaluating our skills.
            </p>
            <p class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4 font-semibold">
              Can we find a
              movie
              that pleases everyone, from the average viewer to the most sophisticated cinephile?
            </p>
            <p>
              This is the challenge we
              aim
              to conquer. Our initial task is to ascertain whether their tastes differ significantly. Let's examine what
              needs
              to be done to achieve this.
            </p>
          </div>
          <img src="/remy.png" alt="remy"
            class="w-[180px] lg:w-[180px] mt-4 drop-shadow-xl lg:max-h-none hover:scale-105 hover:drop-shadow-none transition duration-300 mx-auto lg:ml-8" />
        </div>




        <section id="fridge" class="section  text-justify">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2 ">
            <BookmarkIcon class="w-9 h-9" />What's in our fridge
          </h3>
          <p class="mt-4">
            Let's look at what is available to us.
          </p>
          <h6 class="text-lg font-bold mt-4">CMU Movies</h6>
          <p class="mt-2">
            The base of this analysis is the <a class="text-red-900 underline hover:text-red-400"
              href="http://www.cs.cmu.edu/~ark/personas/" target="_blank">CMU
              dataset</a>, in which the following ingredients are of
            interest:
          <ul class="list-disc list-inside ml-5 my-2 underline">
            <li><a href="#countries">Countries</a></li>
            <li><a href="#genres">Genres</a></li>
            <li><a href="#release-year">Release year</a></li>
            <li><a href="#actors">Actors</a></li>
          </ul>
          We also got the IMDb
          rating from the available dataset on <a class="text-red-900 underline hover:text-red-400"
            href="https://datasets.imdbws.com/">IMDb's
            website</a> and the Metascore from a scrapping of <a href="https://metacritic.com" target="_blank"
            class="text-red-900 underline hover:text-red-400">Metacric</a>.
          </p>
          <p class="mt-2">
            Our processed dataset contains <b>7'770 movies with both IMDb and Metascore ratings</b>.
          </p>

          <h6 class="text-lg font-bold mt-4">Awards</h6>
          <p class="mt-1">
            In addition to that, we also scrapped the awards nominations and wins from <a href="https://www.imdb.com/"
              target="_blank" class="text-red-900 underline hover:text-red-400">IMDb</a> for each movie, in order to
            create the <a href="#awards" class="underline">Awards</a> ingredient.
          </p>

          <h6 class="text-lg font-bold mt-4">Tropes</h6>
          <p class="mt-1">
            And for our last ingredient, we also used <a href="https://github.com/dhruvilgala/tvtropes" target="_blank"
              class="text-red-900 underline hover:text-red-400">an external dataset</a> associating
            tropes to <b>2495 movies</b> out of our 7'770 movies, in order to create the <a href="#tropes"
              class="underline">Tropes</a> ingredient.
          </p>


          <p class="mt-8">
            Before we start cooking, let's take a look at our convives' likings to see if they are similar or not.
          </p>

          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 mt-3">
              <h4 class="text-xl font-bold mt-4">IMDb Users Ratings</h4>
              <p class="mt-2">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium magni quam neque voluptatibus!
                Inventore, praesentium aliquid reiciendis necessitatibus quos iure maxime, unde deserunt hic doloribus
                vitae. Vitae aliquid culpa dolorum?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartUsers" class="aspect-square w-full"></div>
              </div>
            </div>
          </div>


          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 mt-3">
              <h4 class="text-xl font-bold mt-4">Metascore</h4>
              <p class="mt-2">
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corrupti incidunt non, illo assumenda a illum,
                quasi similique nisi, error architecto maxime dolorem. Tempora qui nesciunt tenetur! Quasi esse distinctio
                eveniet.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartMetascore" class="aspect-square w-full"></div>
              </div>
            </div>
          </div>

        </section>

        <section id="cookbook" class="section text-justify">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Statistics Cookbook
          </h3>
          <p class="mt-2">
            We have a lot of tools and nice recipes to use with our ingredients, and we'll try
            to describe and justify them in the following section:
          </p>
          <div>
            <h4 class="text-xl font-bold mt-4">T-Test</h4>
            <p class="mt-2">
              Basic statistics are conducted using the <b>p-value threshold of 0.05</b> to determine if the imdb users and
              metascore
              rating distribution have a significantly different mean.
            </p>
            <h4 class="text-xl font-bold mt-4">Pearson Correlation</h4>
            <p class="mt-2">
              The Pearson correlation will be used systematically on all the features, allowing us to extract a first
              glimpse of which of them is significant on the rating difference. The Pearson correlation measures the
              linear correlation between 2 sets of data, so by measuring the Pearson Correlation Coefficient (PCC) between
              one feature and the rating difference, we will extract the linear correlation between both.
              The significance threshold has been chosen at the <b>p-value of 0.05</b> since it's the most commonly used
              value.
            </p>
            <p class="mt-2">
              In general, the plots will display up to the top and bottom 10 significant features, based on the magnitude
              of the Pearson correlation.
            </p>
            <h4 class="text-xl font-bold mt-4">Ordinary Least Squares (OLS)</h4>
            <p class="mt-2">
              The main tool used throughout the project is the Ordinary Least Square (OLS) regression. The goal of that
              regression is to extract the relative impact of each feature on our variable of interest, the rating
              difference. When relevant, a naive OLS has been conducted and its metrics (F-Statistics, adjusted R^2,
              condition number, …) inspected to judge the relevancy of the model itself, and the results have been
              selected based on their p-value significance, using once more the common <b>p-value threshold of 0.05</b>.
              Nevertheless, OLS regression is not perfect: one of the biggest challenges we faced
              was that it is <b>strongly sensitive to outliers</b> and <b>multicollinear features</b>.
            </p>
            <p class="mt-2">
              When the filtering
              was proved necessary, a second OLS was conducted on the filtered features before being reviewed again to
              assess the improvement.
            </p>
            <p class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4">
              <span class="font-bold">
                Grandma Hack:</span> To detect multicollinear features, one can look at the condition number. Following <a
                target="_blank"
                href="https://github.com/statsmodels/statsmodels/blob/main/statsmodels/regression/linear_model.py#L2843C1-L2844C1"
                class="text-red-900 underline hover:text-red-400">statsmodel's
                official implementation</a>, we can say that if the value is bigger than 1000, there is a huge
              likelihood that a multicollinear feature problem is present!
            </p>
            <h4 class="text-xl font-bold mt-4">Variance Inflation Factor (VIF)</h4>
            <p class="mt-2">
              The VIF is a metric that measures the <b>multicollinearity</b> of a feature. It is calculated by regressing
              each feature against all the other features and then extracting the R^2 of that regression. The VIF is then
              calculated as 1/(1-R^2). The higher the VIF, the higher the multicollinearity. A VIF of 1 means that there
              is no multicollinearity, while a VIF of 5 or more means that there is a strong multicollinearity.
            </p>
            <p class="mt-2">
              In case of multicollinearity, we computed the VIF coefficients of the already pearson significant features
              and filtered out the ones with a VIF higher than 5.
            </p>
          </div>
        </section>

        <section id="noodles" class="section  text-justify">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Instantaneous Noodles and T-Taste
          </h3>
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2">
                The first impression when using raw ingredients is that indeed, the users and critics are not exactly
                appreciating the same things. The following plot shows the distribution of the rating difference between
                the critics and the users.
              </p>
              <p class="mt-4">
                We can learn a few things from this graph. First, we can note that both users and critics seem to have in
                general a similar taste, as there seems to be a positive correlation between both ratings. We can
                nevertheless note that the critic's mean and median are around 60% of the max score and the user's ones
                are around 70% of the max score. We can see that there are some outliers of course, but also that
                sometimes, the critics and the users don't agree, for example, if we take a look at the top left quadrant
                (where users find the movies better than the average and the critics find the movies worse than the
                average) and at the bottom right quadrant (where the users find the movies worse than the average and the
                critics find the movies better than on average).
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartUsersCritics1" class="w-full aspect-square"></div>
              </div>
            </div>
          </div>


          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 mt-3">
              <h4 class="text-xl font-bold mt-4">Rating Difference</h4>
              <p class="mt-2">
                Let's define what we're interested in: <b>the rating difference between the critics and the users</b>.
              </p>
              <p class="mt-4">We can see
                from the following plot that, while this distribution looks normal, it's shifted to the left (as we said
                before the
                user tends to slightly grade more generously than the critics, which means that when making the difference
                we end up with a negative mean).
              </p>
              <p class="mt-4">
                Running classic statistical tools allows us to affirm that those distributions are normal, and more
                interestingly, the <u>rating difference is significant</u>. It's worth studying and analyzing it deeper.
              </p>
              <p class="mt-4">
                Even if this first meal is quite quickly prepared, it raises the question we want to answer: <b>what can
                  explain
                  this discrepancy?</b>
              </p>

              <p class="mt-4">
                Let's open our favorite cookbook and look for recipes that could help us explain that.
              </p>

            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartUsersCritics2" class="w-full aspect-square"></div>
              </div>
            </div>
          </div>


        </section>
      </section>

      <section id="exploration" class="section text-justify">
        <h2 class="text-5xl font-bold mt-8">Time to cook</h2>
        <h5 class="text-2xl italic text-slate-600 mt-1 ml-1">Exploring the ingredients</h5>

        <!-- == COUNTRIES == -->
        <section id="countries" class="section">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Countries
          </h3>
          <p class="mt-6">
            In the grand kitchen of our data-driven analysis, let's craft a narrative as we
            examine the intricate relationship between a film's country of origin and its critical reception. To whet our
            appetites for understanding, we must first visually savor the prepared plots—each a dish to be dissected for
            its unique storytelling flavors.
          </p>

          <div class="grid lg:grid-cols-2 mt-2 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <h4 class="text-xl font-bold mt-8">Visual Appetizer</h4>
              <p class="mt-2">
                This barplot is the first course, served to display the average rating differences by country. The bars
                stretch across the taste spectrum, from the savory highs to the unseasoned lows. The length and direction
                of
                each bar speak to the divergence in cinematic taste—where a film from one country may be the toast of
                critics,
                yet the same film might not suit the public's palate. Countries like France and Italy, with longer bars
                stretching towards the positive side, may suggest a gourmet blend of critical and public agreement. In
                contrast, the United States stands out with a bar extending negatively, indicating a potential
                fast-food-like
                consumption where box office appeal does not translate into critical success.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartCountries1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <div class="grid lg:grid-cols-2 mt-2 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 mt-5">
              <h4 class="mt-4 text-xl font-bold">Pearson Correlation</h4>
              <p class="mt-2">
                The Pearson coefficient plot is the main course, providing a more nuanced flavor profile of each country's
                cinematic output. Each bar, with its confidence interval whiskers, indicates the strength and direction of
                the relationship between a film's country of origin and its rating difference. Notice the subtle hints of
                positive correlations for France and Iran, suggesting that films from these regions carry a certain je ne
                sais quoi that resonates with critics. On the flip side, the United States and Canada show negative
                correlations, implying a different critical reception, perhaps due to the commercial seasoning of their
                film industries.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartCountries2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>


          <div class="grid lg:grid-cols-2 mt-2 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 mt-5">
              <h4 class="mt-2 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
              <p class="mt-2">
                Next to it, we present the OLS coefficients plot, a complementary dish that illustrates the impact of each
                country when other ingredients in our analysis are held constant. Here, Iran's positive coefficient is
                robust, further validating the country's standing with critics. The negative coefficients for powerhouses
                like the United States and India are stark, reinforcing the narrative that commercial success is not a
                guaranteed recipe for critical acclaim.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartCountries3" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <div class="grid mt-8 w-full gap-3">
            <h4 class="text-xl font-bold">Dissecting the Differences in Country
              Coefficients</h4>
            <p>
              Let's delve deeper into the gourmet guide of global cinema by closely examining and comparing the plots
              that serve as our visual menu.
            </p>
            <p>
              Firstly, the Pearson plot offers us a raw measure of the relationship between the country of origin and
              the rating difference. Countries like France, with a correlation of 0.141 and a p-value strikingly close
              to zero, showcase a strong positive alignment with critic ratings. Iran follows suit but with a lesser
              correlation of 0.065, still significant enough to suggest that its films are savored by critics. The plot
              also reveals the statistical significance (p-value) of these relationships, emphasizing the reliability of
              our findings.
            </p>
            <p>
              In contrast, the OLS coefficients plot refines this relationship by controlling for multiple variables.
              Here, we see Iran's coefficient soaring to 7.383, a testament to its films' critical acclaim when other
              factors are constant. This is contrasted by the United States, which sees a negative coefficient of
              -5.8119, painting a picture of a cinematic giant whose films are, perhaps, too rich in mainstream appeal
              for the critic's more selective taste.
            </p>
          </div>


          <h4 class="text-xl font-bold mt-6">Comparative Analysis: Tasting Notes on Methodologies</h4>
          <p class="mt-3">
            Comparing the two plots, we note a shift in the order of countries and the magnitude of their influence.
            For
            example, while France tops the Pearson plot, Iran takes the lead in the OLS analysis, highlighting how
            controlling for other variables can change the taste profile of our data dish.
          </p>
          <p class="mt-3">
            The Pearson method offers simplicity and a direct taste test of correlation, but it can't account for the
            complex mix of ingredients that go into film ratings. It's like tasting a sauce before it's been fully
            seasoned - useful, but not the complete flavor. Its advantages lie in its straightforward interpretation,
            but it falls short by not considering other potentially confounding spices.
          </p>
          <p class="mt-3">
            The OLS method, however, simmers down the data to control for various elements, akin to a slow-cooked stew
            that melds flavors together for a more comprehensive profile. This method allows us to taste the unique
            contribution of each country, but it can be a complex dish to digest, requiring assumptions like linearity
            and normality that may not always hold. One drawback is that significant results can be influenced by
            outliers, just like how a single overpowering spice can skew the taste of a dish.
          </p>
          <h4 class="text-xl font-bold mt-6">Serving the Final Course: Conclusions with a Pinch of Precision</h4>
          <p class="mt-2">
            Next to it, we present the OLS coefficients plot, a complementary dish that illustrates the impact of each
            country when other ingredients in our analysis are held constant. Here, Iran's positive coefficient is
            robust, further validating the country's standing with critics. The negative coefficients for powerhouses
            like the United States and India are stark, reinforcing the narrative that commercial success is not a
            guaranteed recipe for critical acclaim.
          </p>

          <p class="mt-4">
            In the grand dining hall of global cinema, it appears that critics tend to favor films that
            offer a
            distinct cultural voice, complex narratives, and a strong artistic vision—qualities that are often
            highlighted in French and Iranian films. Conversely, industries known for their box office prowess, such as
            Hollywood and Bollywood, might prioritize elements that ensure commercial success—an industry that caters to
            mass appeal rather than the gourmet tastes of critics.
          </p>

          <!-- Tabs -->
          <div class="flex flex-col mt-6 w-full">
            <TabsSection :tabs="countriesTabs" :defaultIndex="5" />
          </div>
        </section>


        <!-- == GENRES == -->
        <section id="genres" class="section">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Genres
          </h3>
          <h5 class="text-xl italic text-slate-600">Crafting the Narrative of Preference</h5>

          <!-- Basic Viz -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 text-justify">
              <div>
                <h4 class="mt-4 text-xl font-bold">Pearson Correlation</h4>
                <p class="mt-2">
                  The first technique in our cookbook is the beloved Pearson correlation. This lovely tool allows us to
                  extract significant genres. Out of 314 genres and subgenres, only <u>61 are significant</u>
                  for
                  our
                  analysis.
                </p>
                <p class="mt-4">
                  Looking a bit more in detail at this plot, the genres exhibited feel way more concrete than
                  before. It's not surprising to see critics liking more <i class="text-red-900 font-semibold">World
                    cinema</i> or <i class="text-red-900 font-semibold">Art film</i>
                  categories.
                  On the other
                  end of the spectrum, <i class="text-red-900 font-semibold">Action</i> films and <i
                    class="text-red-900 font-semibold">Comedy</i> have the support of a wider audience.
                  Interestingly, we do
                  see <i class="text-red-900 font-semibold">Gross-out</i> and <i
                    class="text-red-900 font-semibold">Gross-out films</i> both appear. Why do we see this kind of genre
                  twice with
                  the same
                  result? And even worse: is there something odd behind our analysis?</p>

                <p class="mt-4">
                  While filtering out subgenres would
                  sound natural, it's often in those small niche genres that the critics' tastes were hiding. We took the
                  gambit to keep them at first and filter them later through significance methods if needed. While
                  instructive, we have to work a bit more on our data.
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 text-justify">
              <div>
                <h4 class="mt-4 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                <p class="mt-2">
                  It occured that the first OLS's showed a very high condition number hinting the presence of
                  a strong multicollinearity. This threatened the interpretation of the results and required some VIF
                  filtering. After filtering according to our cookbook, only 93 features were retained and passed again
                  through our OLS.
                  Finally, applying our
                  significance threshold (p-value&lt;0.05), the filtered OLS yields about <u>22 significant genres</u>.
                </p>
                <p class="mt-4">
                  Looking closer at our plot, we see that the previously spotted parasitic genres such as <i
                    class="text-red-900 font-semibold">Gross
                    out</i> have been correctly filtered out, providing a way cleaner overview of what genres impact the
                  rating
                  difference. For the finest gourmet amongst you, the results give an adjusted R^2 of 0.136, meaning that
                  the genres alone can explain up to <b>13.6%</b> of the variance of the rating difference between critics
                  and
                  users.
                </p>
                <p class="mt-4">
                  However, let's stay down-to-earth. The confidence interval around some of these genres triggers a small
                  warning, and for instance, the <i class="text-red-900 font-semibold">Inspirational Drama</i> or <i
                    class="text-red-900 font-semibold">Feminist Film</i> genres shouldn't be judged
                  so fast. This
                  wide confidence interval can partially be explained by the relatively low number of films in those
                  categories.
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres3" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Tabs -->
          <div class="flex flex-col mt-8 w-full gap-5">
            <TabsSection :tabs="genresTabs" :defaultIndex="1" />
          </div>
        </section>

        <!-- === AWARDS === -->
        <section id="awards" class="section text-justify">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Awards
          </h3>
          <!-- Basic Viz -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 mt-5">
              <p class="mt-2">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartAwards1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 mt-3">
              <div>
                <h4 class="mt-4 text-xl font-bold">Pearson Correlation</h4>
                <p class="mt-2">
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Animi culpa, dignissimos consequuntur deserunt
                  maiores voluptas reiciendis pariatur cum? Temporibus ipsum odit in corporis? Nostrum voluptatem magni
                  quo nulla reprehenderit nemo?
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartAwards2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 mt-3">
              <div>
                <h4 class="mt-4 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                <p class="mt-2">
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt saepe, recusandae culpa nisi earum optio
                  laborum temporibus voluptatibus vel aliquid placeat quas non ab ullam deserunt rem incidunt asperiores
                  veritatis!
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartAwards3" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Tabs -->
          <div class="flex flex-col mt-8 w-full gap-5">
            <TabsSection :tabs="awardsTabs" :defaultIndex="6" />
          </div>
        </section>


        <section id="release-year" class="section">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Release Year
          </h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <!-- == ACTORS == -->
        <section id="actors" class="section">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Actors
          </h3>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <div class="mt-4">
                <h4 class="mt-3 text-xl font-bold">Pearson Correlation</h4>
                <p class="mt-2 text-justify">
                  Once again, a rotten tomato could spoil the real taste of the preparation, and we want to avoid such
                  mistakes. Cleaning our ingredient basket with the Pearson correlation gives this yummy plot of <u>426
                    significant</u> actors out of 3151 ones.
                </p>
                <p class="text-justify mt-4">
                  Let's look a bit more in detail at what this shows us. Analyzing the significant actors already gives
                  quite interesting results. We can notice that the best-performing actors for impressing critics are
                  mostly
                  old actors, such as <i class="text-red-900 font-semibold">Cary Grant</i> or <i
                    class="text-red-900 font-semibold">Ward Bond</i>. A small warning here: since those actors are mostly
                  from the
                  beginning of cinema history, their results might be biased. Indeed, it is possible that their less
                  renowned movies or less-performing roles were simply filtered out due to the lack of data. Indeed, a
                  film
                  too old might not even be rated retrospectively by critics and users if it was a forgettable experience.
                  This phenomenon could bias them toward higher scores. This is also to be mitigated by the fact that, in
                  a
                  way, if those actors are still known to experts, they marked cinema history and could deserve their
                  place.
                </p>
                <p class="text-justify mt-4">
                  On the other hand, recent movies and actors are much less likely to be given the chance to not be scored
                  badly for a bad movie. No second chances for <i class="text-red-900 font-semibold">Ryan Reynolds</i> or
                  <i class="text-red-900 font-semibold">Ashton Kutcher</i>. Indeed, alternating between
                  deep roles highlighting their talent and lighter characters might be detrimental to them in this plot.
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartActors1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 text-justify">
              <div class="mt-4">
                <h4 class="mt-4 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                <p class="mt-2 ">
                  Running the OLS gives once more insightful results, with an adjusted R^2 of 0.13 (<b>13%</b>). Having
                  specific actors
                  seems then to be impactful on the results, with the <u>20 significant</u> ones shown in this plot.
                </p>
                <p class="mt-4">Once
                  again, the variances are quite big, probably due to the relatively low number of films each actor's been
                  in compared to the total number of films and actors. A final remark must be noted too: we can't be sure
                  that the genres and the actors are not entangled in a way. Some actors are probably performing well in
                  specific genres while being considered awful in others. Sadly, we've been unable to completely rule out
                  that kind of confounding effect, since all of the features we have are of course strongly
                  interconnected.
                </p>
                <p class="mt-4">
                  Comparing the result of the Pearson shows that the results seem comparable, with some slight difference
                  in
                  the order. The type of the actors, however, seem quite consistent between the two.
                </p>
              </div>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartActors2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Tabs -->
          <div class="flex flex-col mt-8 w-full gap-5">
            <TabsSection :tabs="actorsTabs" :defaultIndex="3" />
          </div>
        </section>

        <!-- == TROPES == -->
        <section id="tropes" class="section">
          <h3 class="text-4xl font-bold mt-8 flex items-end gap-2">
            <BookmarkIcon class="w-9 h-9" />Tropes
          </h3>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-2 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 mt-3">
              <h4 class="mt-4 text-xl font-bold">Pearson Correlation</h4>
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartTropes1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-2 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 mt-5">
              <h4 class="mt-4 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartTropes2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <div class="flex flex-col mt-8 w-full gap-5">
            <TabsSection :tabs="tropesTabs" :defaultIndex="4" />
          </div>
        </section>
      </section>

      <section id="conclusion" class="section">
        <h2 class="text-5xl font-bold mt-8 mb-6">Conclusion</h2>
        <p class="mt-2 text-justify">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
          consequat
          aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl.
        </p>

        <!-- Pearson -->
        <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
          <div class="flex flex-col order-2 lg:order-2">
            <h4 class="mt-4 text-xl font-bold">Pearson Correlation</h4>
            <p class="mt-2 text-justify">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
              cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
              repellendus laboriosam laudantium. Esse, facilis?
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
              eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
              suscipit magnam?
            </p>
          </div>
          <div class="flex flex-col order-1 lg:order-1 w-full">
            <div class="flex flex-col h-full w-full">
              <div ref="chartGlobal1" class="h-full min-h-[600px] w-full"></div>
            </div>
          </div>
        </div>

        <!-- OLS -->
        <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
          <div class="flex flex-col order-2 lg:order-1">
            <h4 class="mt-4 text-xl font-bold">Ordinary Least Squares (OLS)</h4>
            <p class="mt-2 text-justify">
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
              cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
              repellendus laboriosam laudantium. Esse, facilis?
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
              eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
              suscipit magnam?
            </p>
          </div>
          <div class="flex flex-col order-1 lg:order-2 w-full">
            <div class="flex flex-col h-full w-full">
              <div ref="chartGlobal2" class="h-full min-h-[600px] w-full"></div>
            </div>
          </div>
        </div>

        <div class="grid lg:grid-cols-3 mt-8 w-full gap-5">
          <div class="flex flex-col order-2 lg:order-1 col-span-2">
            <p class="mt-3">
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus id, quod veritatis eos laboriosam omnis
              quas. Impedit aut, odit possimus iusto error mollitia voluptatem, esse numquam eveniet reprehenderit, veniam
              commodi.
            </p>
          </div>
          <div class="flex flex-col col-span-3 order-1 lg:col-span-1 lg:order-2 w-full items-center justify-center">
            <div class="flex flex-col h-full w-full items-center justify-center">
              <img src="/ego.png" alt="ego"
                class="lg:w-full mt-4 drop-shadow-xl max-h-[400px] lg:max-h-none hover:scale-y-105 hover:-scale-x-105 hover:drop-shadow-none transition duration-300 -scale-x-100" />
            </div>
          </div>
        </div>


      </section>

      <section id="playground" class="section">
        <h2 class="text-5xl font-bold mt-8">Playground</h2>
        <div>
          <Playground />
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.section {
  padding-top: 50px;
  margin-top: -50px;
}

.lamp-container {
  position: relative;
}


.lamp {
  width: 200px;
  /* Adjust as per your image size */
  display: block;
  z-index: 2;
  left: 0;
  position: relative;
  height: auto;
}

.light-aura {
  position: absolute;
  top: 0;
  left: 0;
  /* Start the aura right at the end of the lamp */
  /* Extend to the rest of the viewport */
  height: 300vh;
  z-index: 1;
  opacity: 0.5;
  /* Ensures the light aura is behind the lamp */
}
</style>



<script setup>
import { onMounted, ref, defineAsyncComponent } from 'vue';
import Plotly from 'plotly.js-basic-dist-min'
import { BookmarkIcon } from "@heroicons/vue/24/solid"
const BASE_URL = import.meta.env.VITE_BASE_URL;


const Navbar = defineAsyncComponent(() => import('./Navbar.vue'));
const Playground = defineAsyncComponent(() => import('./Playground.vue'));
const TabsSection = defineAsyncComponent(() => import('./TabsSection.vue'));

const chartUsers = ref(null);
const chartMetascore = ref(null);
const chartUsersCritics1 = ref(null);
const chartUsersCritics2 = ref(null);
const chartCountries1 = ref(null);
const chartCountries2 = ref(null);
const chartCountries3 = ref(null);
const chartGenres1 = ref(null);
const chartGenres2 = ref(null);
const chartGenres3 = ref(null);
const chartAwards1 = ref(null);
const chartAwards2 = ref(null);
const chartAwards3 = ref(null);
const chartActors1 = ref(null);
const chartActors2 = ref(null);
const chartTropes1 = ref(null);
const chartTropes2 = ref(null);
const chartGlobal1 = ref(null)
const chartGlobal2 = ref(null)

const countriesTabs = ref(null)
const genresTabs = ref(null)
const awardsTabs = ref(null)
const tropesTabs = ref(null)
const actorsTabs = ref(null)

const activeLamp = ref(true)

const flareColorScale = [
  [0, '#f6e8c3'],
  [0.28, '#fddbc7'],
  [0.42, '#f4a582'],
  [0.56, '#d6604d'],
  [0.70, '#b2182b'],
  [1.0, '#67001f']
];

const fetchData = async (path) => {
  const originUrl = window.location.origin;

  if (BASE_URL && BASE_URL !== '/') return await fetch(`${originUrl}/${BASE_URL}/${path}`).then(response => response.json());

  return await fetch(`${originUrl}/${path}`).then(response => response.json());

};

function stringDivider(str, width, spaceReplacer) {
  if (str.length > width) {
    var p = width
    for (; p > 0 && str[p] != ' '; p--) {
    }
    if (p > 0) {
      var left = str.substring(0, p);
      var right = str.substring(p + 1);
      return left + spaceReplacer + stringDivider(right, width, spaceReplacer);
    }
  }
  return str;
}

function plotChart(chartRef, data, layout) {
  Plotly.newPlot(chartRef.value, data, layout);
}

function transformDataForPlotly(data, x_column, y_column, error_x_column, text_function = null) {
  let maxValue = data.length - 1;
  let trace = {
    x: data.map(item => item[x_column]),
    y: data.map(item => item[y_column]),
    hovertext: text_function ? data.map(item => text_function(item)) : null,
    error_x: {
      type: 'data',
      array: data.map(item => item[error_x_column]),
      visible: true
    },
    type: 'bar',
    orientation: 'h',
    marker: {
      color: data.map((_, index) => index / maxValue), // Assign a normalized value based on index
      colorscale: flareColorScale
    },
  };
  return [trace];
}

onMounted(async () => {

  const countries1 = await fetchData('/data/countries-1.json');
  const countries2 = await fetchData('/data/countries-2.json');
  const countries3 = await fetchData('/data/countries-3.json');
  const genres1 = await fetchData('/data/genres-1.json');
  const genres2 = await fetchData('/data/genres-2.json');
  const genres3 = await fetchData('/data/genres-3.json');
  const awards1 = await fetchData('/data/awards-1.json');
  const awards2 = await fetchData('/data/awards-2.json');
  const awards3 = await fetchData('/data/awards-3.json');
  const actors1 = await fetchData('/data/actors-1.json');
  const actors2 = await fetchData('/data/actors-2.json');
  const tropes1 = await fetchData('/data/tropes-1.json');
  const tropes2 = await fetchData('/data/tropes-2.json');
  const global1 = await fetchData('/data/global-1.json');
  const global2 = await fetchData('/data/global-2.json');
  const movies = await fetchData('/data/playground-movies.json');

  tropesTabs.value = await fetchData('/data/tropesTabs.json')
  countriesTabs.value = await fetchData('/data/countriesTabs.json')
  genresTabs.value = await fetchData('/data/genresTabs.json')
  actorsTabs.value = await fetchData('/data/actorsTabs.json')
  awardsTabs.value = await fetchData('/data/awardsTabs.json')

  // Example function to calculate bins and counts
  function calculateBins(data, binSize) {
    let min = Math.min(...data);
    let max = Math.max(...data);
    let bins = [];
    let counts = {};

    // Create bins
    for (let i = min; i <= max; i += binSize) {
      bins.push(i);
      counts[i] = 0;
    }

    // Count data points in each bin
    data.forEach(value => {
      let bin = Math.floor(value / binSize) * binSize;
      counts[bin] = (counts[bin] || 0) + 1;
    });

    return counts;
  }

  // Users Bar Chart
  if (chartUsers) {

    const imdb_ratings_counts = calculateBins(movies.map(item => item.imdb_rating_scaled / 10), 0.5)
    const trace = [{
      x: Object.keys(imdb_ratings_counts),
      y: Object.values(imdb_ratings_counts),
      name: 'Count',
      type: 'bar',
      marker: {
        color: '#d6604d',
        line: {
          color: '#d6604d',
          width: 10
        }
      },
      opacity: 0.75
    }, {
      x: [movies.map(item => item.imdb_rating_scaled / 10).reduce((a, b) => a + b, 0) / movies.length],
      y: [Math.max(...Object.values(imdb_ratings_counts))],
      type: 'bar',
      name: 'Mean',
      marker: {
        color: 'red',
        line: {
          color: 'red',
          width: 0.5
        }
      }
    }, {
      x: [movies.map(item => item.imdb_rating_scaled / 10).sort((a, b) => a - b)[Math.floor(movies.length / 2)]],
      y: [Math.max(...Object.values(imdb_ratings_counts))],
      type: 'bar',
      name: 'Median',
      marker: {
        color: 'blue',
        line: {
          color: 'blue',
          width: 0.5
        }
      },
      opacity: 1
    }]

    plotChart(chartUsers, trace, {
      title: 'IDMb Average Users Rating',
      xaxis: {
        title: 'Users Rating',
        automargin: true,
        range: [0, 11]
      },
      yaxis: {
        title: 'Movies (count)',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Metascore Bar Chart 
  if (chartMetascore) {
    const metascore_counts = calculateBins(movies.map(item => item.metascore), 5)

    const trace = [{
      x: Object.keys(metascore_counts),
      y: Object.values(metascore_counts),
      name: 'Count',
      type: 'bar',
      marker: {
        color: '#d6604d',
        line: {
          color: '#d6604d',
          width: 10
        }
      },
      opacity: 0.75
    }, {
      x: [movies.map(item => item.metascore).reduce((a, b) => a + b, 0) / movies.length],
      y: [Math.max(...Object.values(metascore_counts))],
      type: 'bar',
      name: 'Mean',
      marker: {
        color: 'red',
        line: {
          color: 'red',
          width: 0.25
        }
      }
    }, {
      x: [movies.map(item => item.metascore).sort((a, b) => a - b)[Math.floor(movies.length / 2)]],
      y: [Math.max(...Object.values(metascore_counts))],
      type: 'bar',
      name: 'Median',
      marker: {
        color: 'blue',
        line: {
          color: 'blue',
          width: 0.25
        }
      },
      opacity: 1
    }]

    plotChart(chartMetascore, trace, {
      title: 'Metascores',
      xaxis: {
        title: 'Metascore',
        automargin: true,
        range: [0, 105]
      },
      yaxis: {
        title: 'Movies (count)',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Users vs Critics Scatter
  if (chartUsersCritics1) {
    const trace = [{
      x: movies.map(movie => movie.metascore),
      y: movies.map(movie => movie.imdb_rating_scaled),
      mode: 'markers',
      type: 'scatter',
      hovertext: movies.map(movie => movie.name),
      marker: {
        color: '#67001f',
        opacity: 0.2
      }
    }, {
      x: [0, 105],
      y: [0, 105],
      mode: 'lines',
      type: 'scatter',
      name: 'x=y',
      line: {
        dash: 'dot',
        width: 2,
        color: 'grey'
      }
    }, {
      x: [movies.map(movie => movie.metascore).reduce((a, b) => a + b, 0) / movies.length],
      y: [movies.map(movie => movie.imdb_rating_scaled).reduce((a, b) => a + b, 0) / movies.length],
      mode: 'markers',
      type: 'scatter',
      name: 'Mean',
      marker: {
        color: 'red',
        line: {
          color: 'red',
          width: 2
        }
      }
    }, {
      x: [movies.map(movie => movie.metascore).sort((a, b) => a - b)[Math.floor(movies.length / 2)]],
      y: [movies.map(movie => movie.imdb_rating_scaled).sort((a, b) => a - b)[Math.floor(movies.length / 2)]],
      mode: 'markers',
      type: 'scatter',
      name: 'Median',
      marker: {
        color: 'blue',
        line: {
          color: 'blue',
          width: 2
        }
      },
      opacity: 1
    }];

    const layout = {
      title: "IMDb Users Rating vs Metascore",
      xaxis: {
        range: [0, 105],
        title: 'Metascore',
        automargin: true
      },
      yaxis: {
        range: [0, 105],
        title: 'IMDB Users Rating Scaled',
        scaleratio: 1,
        automargin: true
      },
      margin: {
        l: 70,
        r: 50,
        b: 70,
        t: 50,
        pad: 4
      },
      showlegend: false
    };

    plotChart(chartUsersCritics1, trace, layout)
  }

  // User vs Critics 2
  if (chartUsersCritics2) {
    const rating_difference_counts = calculateBins(movies.map(item => item.rating_difference), 5)

    const trace = [{
      x: Object.keys(rating_difference_counts),
      y: Object.values(rating_difference_counts),
      type: 'bar',
      name: 'Count',
      marker: {
        color: '#d6604d',
        line: {
          color: '#d6604d',
          width: 5
        }
      },
      opacity: 0.75
    }, {
      x: [movies.map(item => item.rating_difference).reduce((a, b) => a + b, 0) / movies.length],
      y: [Math.max(...Object.values(rating_difference_counts))],
      type: 'bar',
      name: 'Mean',
      marker: {
        color: 'red',
        line: {
          color: 'red',
          width: 2
        }
      }
    }, {
      x: [movies.map(item => item.rating_difference).sort((a, b) => a - b)[Math.floor(movies.length / 2)]],
      y: [Math.max(...Object.values(rating_difference_counts))],
      type: 'bar',
      name: 'Median',
      marker: {
        color: 'blue',
        line: {
          color: 'blue',
          width: 2
        }
      },
      opacity: 1

    }]

    plotChart(chartUsersCritics2, trace, {
      title: 'Rating Differences',
      xaxis: {
        title: 'Rating Difference',
        automargin: true,
        range: [-105, 105]
      },
      yaxis: {
        title: {
          text: 'Movies (count)',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }


  // Countries 1
  if (chartCountries1) {
    countries1.sort((a, b) => {
      return a.mean - b.mean;
    });

    const trace = transformDataForPlotly(countries1, 'mean', 'countries', 'sem', function (item) {
      return `Number of movies: ${item.count.toFixed(0)}`;
    })

    plotChart(chartCountries1, trace, {
      title: 'Mean Rating difference for Countries',
      xaxis: {
        title: 'Rating difference',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Country',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Countries 2
  if (chartCountries2) {
    countries2.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    const trace = transformDataForPlotly(countries2, 'correlation', 'Country', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartCountries2, trace, {
      title: 'Pearson correlation for Countries',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Country',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Countries 3
  if (chartCountries3) {
    countries3.sort((a, b) => {
      return a.coef - b.coef;
    });
    const trace = transformDataForPlotly(countries3, 'coef', 'Country', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartCountries3, trace, {
      title: 'OLS coefficient for Countries',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Country',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 1
  if (chartGenres1) {
    genres1.sort((a, b) => {
      return a.rating_difference - b.rating_difference;
    });

    // keep the top 10 and bottom 10
    let bottom = genres1.slice(0, 10);
    let top = genres1.slice(-10);
    let genres1_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(genres1_filtered, 'rating_difference', 'genres', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}`;
    })

    plotChart(chartGenres1, trace, {
      title: 'Mean rating difference for Genres',
      xaxis: {
        title: 'Rating difference',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Genre',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 2
  if (chartGenres2) {
    genres2.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    let top = genres2.slice(-10);
    let bottom = genres2.slice(0, 10);
    let genres2_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(genres2_filtered, 'correlation', 'Genre', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartGenres2, trace, {
      title: 'Pearson correlation for Genres',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Genre',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 3
  if (chartGenres3) {
    genres3.sort((a, b) => {
      return a.coef - b.coef;
    });

    const trace = transformDataForPlotly(genres3, 'coef', 'Genre', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartGenres3, trace, {
      title: 'OLS coefficient for Genres',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Genre',
          standoff: 0
        },
        automargin: true,
        ticklen: 10,
        tickcolor: 'white'
      },
      autosize: true,
      responsive: true,
    });
  }

  // Awards 1
  if (chartAwards1) {
    awards1.sort((a, b) => {
      return a.number_of_movies - b.number_of_movies;
    });

    // keep the top 10 and bottom 10
    let bottom = awards1.slice(0, 10);
    let top = awards1.slice(-10);
    let awards1_filtered = bottom.concat(top);

    const trace = [{
      x: awards1_filtered.map(item => item.number_of_movies),
      y: awards1_filtered.map(item => stringDivider(item.awards_received, 20, "<br>")),
      type: 'bar',
      hovertext: awards1_filtered.map(item => `Number of movies: ${item.number_of_movies.toFixed(0)}`),
      marker: {
        color: '#67001f'
      },
      opacity: 0.75,
      orientation: 'h',

    }]

    plotChart(chartAwards1, trace, {
      title: 'Mean rating difference for Awards',
      xaxis: {
        title: 'Rating difference',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Award',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Awards 2
  if (chartAwards2) {
    awards2.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    const maxValue = awards2.length - 1;

    const trace = [{
      x: awards2.map(item => item.correlation),
      y: awards2.map(item => stringDivider(item['Awards'], 20, "<br>")),
      type: 'bar',
      hovertext: awards2.map(item => `P-value: ${item.p_value}`),
      marker: {
        color: awards2.map((_, index) => index / maxValue), // Assign a normalized value based on index
        colorscale: flareColorScale
      },
      opacity: 0.75,
      orientation: 'h',
    }]

    plotChart(chartAwards2, trace, {
      title: 'Pearson correlation for Awards',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Award',
          standoff: 10
        },
        automargin: true,
        ticklen: 10,
        tickcolor: 'white'
      },
      autosize: true,
      responsive: true,
    });
  }

  // Awards 3
  if (chartAwards3) {
    awards3.sort((a, b) => {
      return a.coef - b.coef;
    });

    const maxValue = awards3.length - 1;

    const trace = [{
      x: awards3.map(item => item.coef),
      y: awards3.map(item => stringDivider(item['Awards'], 20, "<br>")),
      type: 'bar',
      hovertext: awards3.map(item => `P-value: ${item.p_value}`),
      marker: {
        color: awards3.map((_, index) => index / maxValue), // Assign a normalized value based on index
        colorscale: flareColorScale
      },
      opacity: 0.75,
      orientation: 'h',
    }]

    plotChart(chartAwards3, trace, {
      title: 'OLS coefficient for Awards',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Award',
          standoff: 10
        },
        automargin: true,
        ticklen: 10,
        tickcolor: 'white'
      },
      autosize: true,
      responsive: true,
    });
  }

  // Actors 1
  if (chartActors1) {
    actors1.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    // keep the top 10 and bottom 10
    let bottom = actors1.slice(0, 10);
    let top = actors1.slice(-10);
    let actors1_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(actors1_filtered, 'correlation', 'actor_name', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartActors1, trace, {
      title: 'Pearson correlation for Actors',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Actor',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Actors 2
  if (chartActors2) {
    actors2.sort((a, b) => {
      return a.coef - b.coef;
    });

    const trace = transformDataForPlotly(actors2, 'coef', 'actor_name', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartActors2, trace, {
      title: 'OLS coefficient for Actors',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Actor',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Tropes 1
  if (chartTropes1) {
    tropes1.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    // keep the top 10 and bottom 10
    let bottom = tropes1.slice(0, 10);
    let top = tropes1.slice(-10);
    let tropes1_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(tropes1_filtered, 'correlation', 'Trope', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartTropes1, trace, {
      title: 'Pearson correlation for Tropes',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Trope',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Tropes 2
  if (chartTropes2) {
    tropes2.sort((a, b) => {
      return a.coef - b.coef;
    });

    let top = tropes2.slice(-10);
    let bottom = tropes2.slice(0, 10);
    let tropes2_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(tropes2_filtered, 'coef', 'Trope', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartTropes2, trace, {
      title: 'OLS coefficient for Tropes',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Trope',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }


  // Global 1
  if (chartGlobal1) {
    global1.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    // keep the top 10 and bottom 10
    let global1_filtered = global1;
    if (global1.length > 20) {
      let bottom = global1.slice(0, 10);
      let top = global1.slice(-10);
      global1_filtered = bottom.concat(top);
    }

    const trace = transformDataForPlotly(global1_filtered, 'correlation', 'Feature', 'sem', function (item) {
      return `P-value: ${item.p_value}`;
    })

    plotChart(chartGlobal1, trace, {
      title: 'Pearson correlation for global features',
      xaxis: {
        title: 'Pearson correlation',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Feature',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Global 2
  if (chartGlobal2) {
    global2.sort((a, b) => {
      return a.coef - b.coef;
    });

    let global2_filtered = global2
    if (global2.length > 20) {
      let top = global2.slice(-10);
      let bottom = global2.slice(0, 10);
      global2_filtered = bottom.concat(top);
    }

    const trace = transformDataForPlotly(global2_filtered, 'coef', 'Feature', 'sem', function (item) {
      return `P-value: ${item.p_value}`;
    })

    plotChart(chartGlobal2, trace, {
      title: 'OLS coefficient for global features',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: {
          text: 'Feature',
          standoff: 0
        },
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }
});

</script>