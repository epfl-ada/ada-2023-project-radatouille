<template>
    <!-- == HERO == -->
    <div
        class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
        <h1 class="text-3xl lg:text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">
            Screen Tastes: The User-Critic Divide in Cinema
        </h1>
        <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain
            movie
            taste differences between users and critics</h3>
        <div class="flex flex-col items-center mt-auto px-5 py-3">
            <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] mt-3 text-center">A project served by the
                Team
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
        <div
            class="flex col-span-5 px-10 lg:px-8 lg:col-span-3 lg:col-start-2 flex-col py-8 w-full mx-auto max-w-screen-lg">
            <section id="introduction" class="section">
                <h2 class="text-4xl lg:text-5xl font-bold mt-5">Introduction</h2>
                <div>
                    <p class="text-justify mt-4 lg:max-w-screen-md">
                        As it's often said, “there is no accounting for taste”. But as flavor explorers and taste
                        crafters, we do care about it. And as much as you're a fan of Brussels Sprouts, everybody is not.
                        Same goes for <b>movies</b>, and a finer palate might find delicacy in other dishes than your
                        favorite
                        pasta al pesto. World renowned <b>critics</b> might disagree with <b>you</b>. But why? Is this
                        difference in
                        taste real? Are the critics overly sophisticated, and like Anton Ego, do they like the
                        simplicity of a simple well cooked dish in the end?
                    </p>
                    <p class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4 font-semibold">
                        Do critics and users have different tastes, and if yes, can we explain it?
                    </p>
                    <p>
                        Or is this discrepancy based on something more concrete? That's the question we want to address,
                        using all the craftsmanship our kitchen brigade freshly learned. From the selection of our
                        ingredients basket to the concoction of our dish, grab your chef's hat and embark with us in
                        this flavorful journey!
                    </p>
                </div>
                <h5 class="text-xl lg:text-2xl mt-4 font-semibold ml-1">The <span
                        class="italic font-semibold">Brigade</span></h5>
                <div class="grid gap-5 lg:gap-3 grid-cols-2 md:grid-cols-3 lg:grid-cols-6">
                    <div class="w-full flex flex-col h-full relative">
                        <img src="/remy.png" alt="remy" class="w-full mt-4 drop-shadow-xl object-contain lg:max-h-none" />
                        <h5 class="font-semibold text-center">Remy</h5>
                    </div>
                    <div class="w-full flex flex-col h-full mt-10">
                        <div class="w-full relative hover:rotate-[-5deg] transition duration-300 hover:scale-105">
                            <img src="/toque.png" alt="toque"
                                class="absolute -top-[48%] left-[35%] w-[50%] h-full object-contain lg:max-h-none z-[2] -scale-x-100" />
                            <img src="/antonin2.jpg" alt="antonin"
                                class="flex w-full drop-shadow-xl object-contain aspect-square rounded-xl mb-2" />
                        </div>
                        <h5 class="font-semibold text-center">Antonin Faure</h5>
                        <h6 class="text-center italic">Master in Data Science</h6>
                    </div>

                    <div class="w-full flex flex-col h-full mt-6 md:mt-10">
                        <div class="w-full relative hover:rotate-[5deg] transition duration-300 hover:scale-105">
                            <img src="/toque.png" alt="toque"
                                class="absolute -top-[46%] rotate-[14deg] left-[44%] w-[50%] h-full object-contain lg:max-h-none z-[2]" />
                            <img src="/baptiste.jpg" alt="baptiste"
                                class="flex w-full drop-shadow-xl object-contain aspect-square rounded-xl mb-2" />
                        </div>
                        <h5 class="font-semibold text-center">Baptiste Lecoeur</h5>
                        <h6 class="text-center italic">Master in Data Science</h6>
                    </div>
                    <div class="w-full flex flex-col h-full mt-6 md:mt-10">
                        <div class="w-full relative hover:rotate-[-5deg] transition duration-300 hover:scale-105">
                            <img src="/toque.png" alt="toque"
                                class="absolute -top-[48%] left-[14%] rotate-[-30deg] w-[65%] -scale-x-100 h-full object-contain lg:max-h-none z-[2]" />
                            <img src="/enzo.jpeg" alt="enzo"
                                class="flex w-full drop-shadow-xl object-contain aspect-square rounded-xl mb-2" />
                        </div>
                        <h5 class="font-semibold text-center">Enzo Palmisano</h5>
                        <h6 class="text-center italic">Master in Energy</h6>
                    </div>
                    <div class="w-full flex flex-col h-full md:mt-10">
                        <div class="w-full relative hover:rotate-[5deg] transition duration-300 hover:scale-105">
                            <img src="/toque.png" alt="toque"
                                class="absolute -top-[37%] left-[18%] rotate-[8deg] w-[45%] h-full object-contain lg:max-h-none z-[2]" />
                            <img src="/jamil.jpeg" alt="jamil"
                                class="flex w-full drop-shadow-xl object-contain aspect-square rounded-xl mb-2" />
                        </div>
                        <h5 class="font-semibold text-center">Jamil Maj</h5>
                        <h6 class="text-center italic">Master in Energy</h6>
                    </div>
                    <div class="w-full flex flex-col h-full md:mt-10">
                        <div class="w-full relative hover:rotate-[-5deg] transition duration-300 hover:scale-105">
                            <img src="/toque.png" alt="toque"
                                class="absolute -top-[34%] left-[23%] rotate-[-30deg] w-[50%] -scale-x-100 h-full object-contain lg:max-h-none z-[2]" />
                            <img src="/mariella.jpeg" alt="mariella"
                                class="flex w-full drop-shadow-xl object-contain aspect-square rounded-xl mb-2" />
                        </div>
                        <h5 class="font-semibold text-center">Mariella Daghfal</h5>
                        <h6 class="text-center italic">Master in Digital Humanities</h6>
                    </div>
                </div>

                <section id="fridge" class="section text-justify">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start gap-2 ">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 mt-1" />What's in our fridge
                    </h3>
                    <p class="mt-4">
                        Let's look at what is available to us.
                    </p>
                    <div class="flex flex-col lg:flex-row gap-5">
                        <img src="/fridge.png" alt="fridge"
                            class="max-w-[200px] mx-auto lg:max-w-[200px] object-contain mt-4 mb-auto drop-shadow-xl hover:scale-105 hover:drop-shadow-none transition duration-300" />
                        <div class="mt-6">
                            <h6 class="text-lg font-bold">CMU Movies</h6>
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
                                website</a> and the Metascore from scrapping <a href="https://metacritic.com"
                                target="_blank" class="text-red-900 underline hover:text-red-400">Metacric</a>.
                            </p>
                            <p class="mt-2">
                                Our processed dataset contains <b>7'770 movies with both IMDb and Metascore ratings</b>.
                            </p>

                            <h6 class="text-lg font-bold mt-4">Awards</h6>
                            <p class="mt-1">
                                In addition to that, we also scrapped the awards nominations and wins from <a
                                    href="https://www.imdb.com/" target="_blank"
                                    class="text-red-900 underline hover:text-red-400">IMDb</a> for each movie, to
                                create the <a href="#awards" class="underline">Awards</a> ingredient.
                            </p>

                            <h6 class="text-lg font-bold mt-4">Tropes</h6>
                            <p class="mt-1">
                                For our last ingredient, we also used <a href="https://github.com/dhruvilgala/tvtropes"
                                    target="_blank" class="text-red-900 underline hover:text-red-400">an external
                                    dataset</a>
                                associating
                                tropes to <b>2495 movies</b> out of our 7'770 movies, to create the <a href="#tropes"
                                    class="underline">Tropes</a> ingredient.
                            </p>
                        </div>
                    </div>


                    <p class="mt-8">
                        Before we start cooking, let's take a look at our convives' likings to see if they are similar or
                        not.
                    </p>

                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <h4 class="text-xl font-bold">IMDb Users Ratings</h4>
                            <p class="mt-2">
                                The IMDb rating consists of a grade between 0 and 10. It is an average of the users's
                                ratings, and as we can see, the average rating is around 6.5. The first quartile is at 6,
                                which means that 75% of the ratings are over 6, so the users don't seem to rate badly
                            </p>
                            <p class="mt-2">
                                For the sake of computing the rating difference, we will use a <b>scaled</b> version of
                                the rating, so that the rating is between 0 and 100, like the Metascore.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartUsers" class="aspect-square w-full"></div>
                            </div>
                        </div>
                    </div>


                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Metascore</h4>
                            <p class="mt-2">
                                The Metascore is an aggregated score resuming the rating of multiple publishers. It consists
                                of a <b>normalized</b> (so relative to the other performances), <b>weighted</b> (as each
                                publisher
                                rates
                                differently) <b>average</b> of the scaled (as each critic rates with a different scale)
                                ratings.
                            </p>
                            <p class="mt-2">
                                The distribution looks <i>quasi-normal</i> (which sounds
                                logical,
                                because as said before, the scores are normalized, and we have a consequent subset of them),
                                with an average of around 60, which means that the <b>critics on average are more difficult
                                    than the users!</b>
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartMetascore" class="aspect-square w-full"></div>
                            </div>
                        </div>
                    </div>

                </section>

                <section id="cookbook" class="section text-justify">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start gap-2 ">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Statistics Cookbook
                    </h3>
                    <p class="mt-2">
                        We have a lot of tools and nice recipes to use with our ingredients, and we'll try
                        to describe and justify them in the following cookbook:
                    </p>
                    <div>
                        <TabGroup :selectedIndex="activeCookbookTabId">
                            <TabList class="bg-red-900 p-2 rounded-xl" v-show="false">
                                <Tab as="button" :key="0"
                                    class="py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': activeCookbookTabId === 0 }"
                                    @click="() => { activeCookbookTabId = 1; }" :show="false">
                                    Cover
                                </Tab>
                                <Tab as="button" :key="1"
                                    class="py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': activeCookbookTabId === 1 }"
                                    @click="() => { activeCookbookTabId = 2; }" :show="false">
                                    T-Test
                                </Tab>
                                <Tab as="button" :key="2"
                                    class="py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': activeCookbookTabId === 2 }"
                                    @click="() => { activeCookbookTabId = 3; }" :show="false">
                                    Pearson Correlation
                                </Tab>
                                <Tab as="button" :key="3"
                                    class="py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': activeCookbookTabId === 3 }"
                                    @click="() => { activeCookbookTabId = 4; }" :show="false">
                                    Ordinary Least Squares (OLS)
                                </Tab>
                                <Tab as="button" :key="4"
                                    class="py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': activeCookbookTabId === 4 }"
                                    @click="() => { activeCookbookTabId = 5; }" v-show="false">
                                    Variance Inflation Factor (VIF)
                                </Tab>
                            </TabList>
                            <div class="flex justify-between mt-6 w-full mx-auto">
                                <button
                                    class="bg-slate-600 hover:bg-slate-700 text-white py-2 px-3 disabled:bg-slate-200 disabled:text-black rounded-l-xl disabled:opacity-0"
                                    @click="activeCookbookTabId -= 1" :disabled="activeCookbookTabId === 0">
                                    &lt;
                                </button>
                                <TabPanels class="w-full h-full">
                                    <TabPanel class="tab-panel h-full w-full">
                                        <TransitionRoot appear :show="activeCookbookTabId === 0" as="template">
                                            <TransitionChild as="template" enter="tab-enter" enter-to="tab-enter-to"
                                                enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to"
                                                leave-from="tab-leave-from">
                                                <div
                                                    class="flex w-full justify-between items-center bg-light h-full object-cover">
                                                    <p class="text-lg italic text-end px-6 w-1/2 hidden lg:block">Turn the
                                                        page...</p>
                                                    <img src="/cookbookCover.png"
                                                        class="flex object-cover w-full lg:w-1/2 border-slate-600 border-l-8" />
                                                </div>
                                            </TransitionChild>
                                        </TransitionRoot>
                                    </TabPanel>
                                    <TabPanel class="tab-panel h-full bg-slate-200">
                                        <TransitionRoot appear :show="activeCookbookTabId == 1" as="template">
                                            <TransitionChild enter="tab-enter" enter-to="tab-enter-to"
                                                enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to"
                                                leave-from="tab-leave-from" as="template">
                                                <div class="flex flex-col lg:flex-row bg-slate-200 w-full h-full">
                                                    <div class="flex flex-col w-full lg:w-1/2 px-5 lg:px-8 h-full py-6 ">
                                                        <h4 class="text-xl font-bold">T-test</h4>
                                                        <p class="mt-2">
                                                            Basic statistics are conducted using the <b>p-value threshold of
                                                                0.05</b> to
                                                            determine if the
                                                            IMDb users and
                                                            Metascore
                                                            rating distribution have a significantly different mean.
                                                        </p>
                                                    </div>
                                                    <div
                                                        class="flex w-full lg:w-1/2 bg-slate-200 lg:border-l-2 border-slate-600">
                                                        <img src="/cookbookTtest.png" alt="ttest"
                                                            class="flex w-full object-contain m-auto max-w-[400px]" />
                                                    </div>
                                                </div>
                                            </TransitionChild>
                                        </TransitionRoot>
                                    </TabPanel>
                                    <TabPanel class="tab-panel h-full bg-slate-200">
                                        <TransitionRoot appear :show="activeCookbookTabId == 2" as="template">
                                            <TransitionChild enter="tab-enter" enter-to="tab-enter-to"
                                                enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to"
                                                leave-from="tab-leave-from" as="template">
                                                <div class="flex flex-col lg:flex-row w-full h-full bg-slate-200">
                                                    <div
                                                        class="flex flex-col px-5 lg:px-8 py-6 bg-slate-200 w-full h-full lg:w-1/2">
                                                        <h4 class="text-xl font-bold">Pearson Correlation</h4>
                                                        <p class="mt-2">
                                                            The Pearson correlation will be used systematically on all the
                                                            features,
                                                            allowing us
                                                            to extract
                                                            a first
                                                            glimpse of which of them is significant on the rating
                                                            difference.
                                                            The
                                                            Pearson
                                                            correlation
                                                            measures the
                                                            linear correlation between 2 sets of data, so by measuring the
                                                            Pearson
                                                            Correlation
                                                            Coefficient
                                                            (PCC) between
                                                            one feature and the rating difference, we will extract the
                                                            linear
                                                            correlation
                                                            between both.
                                                            The significance threshold has been chosen at the <b>p-value of
                                                                0.05</b>
                                                            since
                                                            it's
                                                            the most
                                                            commonly used
                                                            value.
                                                        </p>
                                                        <p class="mt-2">
                                                            In general, the plots will display up to the top and bottom 10
                                                            significant
                                                            features,
                                                            based on
                                                            the magnitude
                                                            of the Pearson correlation.
                                                        </p>
                                                    </div>
                                                    <div
                                                        class="flex w-full lg:w-1/2 bg-slate-200 p-6 lg:border-l-2 border-slate-600">
                                                        <img src="/cookbookPearson.png" alt="pearson"
                                                            class="flex w-full object-contain m-auto max-w-[300px]" />
                                                    </div>
                                                </div>
                                            </TransitionChild>
                                        </TransitionRoot>
                                    </TabPanel>
                                    <TabPanel class="tab-panel bg-slate-200">
                                        <TransitionRoot appear :show="activeCookbookTabId === 3" as="template">
                                            <TransitionChild enter="tab-enter" enter-to="tab-enter-to"
                                                enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to"
                                                leave-from="tab-leave-from" as="template">
                                                <div class="w-full flex flex-col lg:flex-row">
                                                    <div class="px-5 lg:px-8 py-6 bg-slate-200 w-full lg:w-1/2">
                                                        <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                                                        <p class="mt-2">
                                                            The main tool used throughout the project is the Ordinary Least
                                                            Square
                                                            (OLS)
                                                            regression. The
                                                            goal of that
                                                            regression is to extract the relative impact of each feature on
                                                            our
                                                            variable
                                                            of
                                                            interest, the
                                                            rating
                                                            difference. When relevant, a naive OLS has been conducted and
                                                            its
                                                            metrics
                                                            (F-Statistics,
                                                            adjusted R&#178;,
                                                            condition number, ...) inspected to judge the relevancy of the
                                                            model
                                                            itself.
                                                            The
                                                            results have
                                                            been
                                                            selected based on their p-value significance, using once more
                                                            the
                                                            common
                                                            <b>p-value
                                                                threshold of
                                                                0.05</b>.
                                                            Nevertheless, OLS regression is not perfect: one of the biggest
                                                            challenges
                                                            we
                                                            faced
                                                            was that it is <b>strongly sensitive to outliers</b> and
                                                            <b>multicollinear
                                                                features</b>.
                                                        </p>
                                                        <p class="mt-2">
                                                            When the filtering
                                                            was proved necessary, a second OLS was conducted on the filtered
                                                            features
                                                            before
                                                            being reviewed
                                                            again to
                                                            assess the improvement.
                                                        </p>
                                                    </div>
                                                    <div
                                                        class="flex w-full lg:w-1/2 px-0 lg:pr-6 lg:px-6 lg:py-6 lg:border-l-2 border-slate-600">
                                                        <div
                                                            class="bg-white lg:rounded-r-lg lg:border-l-8 border-slate-600 px-6 lg:pr-8 py-4">
                                                            <h4 class="text-xl italic font-semibold mb-1">For the gourmet
                                                            </h4>
                                                            <p>
                                                                The finest chef amongst you may want to know a bit more
                                                                about
                                                                what
                                                                exactly
                                                                we've
                                                                done to get
                                                                an outcome of the OLS. Simply mixing all of the features
                                                                often
                                                                yields a
                                                                bland
                                                                soup. We thus
                                                                refined the model using regularization. The OLS accepts
                                                                Lasso
                                                                (l1)
                                                                and
                                                                Ridge
                                                                (l2)
                                                                regularizations. By tuning a penalty term in the
                                                                optimization
                                                                problem,
                                                                the
                                                                outcomes can be
                                                                cleaner and easier to interpret. In general, Lasso is
                                                                particularly
                                                                indicated
                                                                when a subset
                                                                of the features is expected to not be significant,
                                                                performing a
                                                                sort
                                                                of
                                                                feature
                                                                selection.
                                                                Ridge is more useful to deal with multicollinearity, and can
                                                                help
                                                                keep
                                                                some
                                                                outliers under
                                                                control. Playing with those regularization penalties and
                                                                tuning
                                                                the
                                                                hyperparameter
                                                                <b>alpha</b>
                                                                allows us to produce a refined velouté.
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </TransitionChild>
                                        </TransitionRoot>
                                    </TabPanel>
                                    <TabPanel class="tab-panel bg-slate-200 border-r-8 border-slate-600">
                                        <TransitionRoot appear :show="activeCookbookTabId === 4" as="template">
                                            <TransitionChild enter="tab-enter" enter-to="tab-enter-to"
                                                enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to"
                                                leave-from="tab-leave-from" as="template">
                                                <div class="flex w-full flex-col lg:flex-row">
                                                    <div class="px-5 lg:px-8 py-6 bg-slate-200 w-full lg:w-1/2">
                                                        <h4 class="text-xl font-bold">Variance Inflation Factor (VIF)</h4>
                                                        <p class="mt-2">
                                                            The VIF is a metric that measures the <b>multicollinearity</b>
                                                            of a
                                                            feature. It
                                                            is
                                                            calculated by
                                                            regressing
                                                            each feature against all the other features and then extracting
                                                            the
                                                            R&#178; of
                                                            that
                                                            regression.
                                                            The VIF is
                                                            then
                                                            calculated as :
                                                            <MathJaxEquation :equation="`$$\\frac{1}{1-R^2}$$`" />
                                                            The higher the VIF, the higher the
                                                            multicollinearity. A
                                                            VIF of 1
                                                            means that
                                                            there
                                                            is no multicollinearity, while a VIF of 5 or more means that
                                                            there
                                                            is a
                                                            strong
                                                            multicollinearity.
                                                        </p>
                                                        <p class="mt-2">
                                                            In case of multicollinearity, we computed the VIF coefficients
                                                            of
                                                            the
                                                            already
                                                            Pearson
                                                            significant features
                                                            and filtered out the ones with a VIF higher than 5.
                                                        </p>
                                                    </div>
                                                    <div
                                                        class="flex flex-col w-full lg:w-1/2 px-0 lg:px-6 lg:py-6 lg:border-l-2 border-slate-600">
                                                        <div
                                                            class="bg-white lg:rounded-r-lg lg:border-l-8 border-slate-600 px-5 lg:px-6 lg:pr-8 py-4">
                                                            <p>
                                                                <span class="font-bold">
                                                                    Grandma's Hack:</span> <br>To detect multicollinear
                                                                features, one
                                                                can
                                                                look
                                                                at the
                                                                condition
                                                                number. Following <a target="_blank"
                                                                    href="https://github.com/statsmodels/statsmodels/blob/main/statsmodels/regression/linear_model.py#L2843C1-L2844C1"
                                                                    class="text-red-900 underline hover:text-red-400">statsmodel's
                                                                    official implementation</a>, we can say that if the
                                                                value is
                                                                bigger
                                                                than
                                                                1000,
                                                                there is a
                                                                huge
                                                                likelihood that a multicollinear feature problem is present!
                                                            </p>
                                                            <div class="flex w-1/2 mb-2 mt-10 lg:mt-5 mx-auto relative">
                                                                <img src="/toque.png" alt="toque"
                                                                    class="absolute -top-[40%] left-[32%] rotate-[0deg] w-[50%] -scale-x-100 h-full object-contain lg:max-h-none z-[2]" />
                                                                <img src="/cookbookAda.jpeg" alt="ada"
                                                                    class="w-full mx-auto object-contain my-auto aspect-square rounded-full" />
                                                            </div>
                                                            <h6 class="italic text-center text-lg  font-semibold">Ada
                                                                Lovelace</h6>
                                                            <h6 class="font-light text-sm text-center mb-3">(our
                                                                Grandma)</h6>
                                                        </div>
                                                    </div>
                                                </div>
                                            </TransitionChild>
                                        </TransitionRoot>
                                    </TabPanel>
                                </TabPanels>
                                <button
                                    class="carousel-btn next bg-slate-600 hover:bg-slate-700 text-white py-2 px-3 disabled:bg-slate-200 disabled:text-black rounded-r-xl disabled:opacity-0"
                                    @click="activeCookbookTabId += 1" :disabled="activeCookbookTabId === 4">
                                    &gt;
                                </button>
                            </div>
                        </TabGroup>
                    </div>
                </section>

                <section id="noodles" class="section  text-justify">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Instantaneous Noodles and T-taste
                    </h3>
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <p>
                                The first impression when using raw ingredients is that indeed, the users and critics are
                                not exactly
                                appreciating the same things. The following plot shows the distribution of the rating
                                difference between
                                the critics and the users.
                            </p>
                            <p class="mt-4">
                                We can learn a few things from this graph. First, we can note that both users and critics
                                seem to have in
                                general a similar taste, as there seems to be a positive correlation between both ratings.
                                We can
                                nevertheless note that the critic's mean and median are around 60% of the max score and the
                                user's ones
                                are around 70% of the max score. We can see that there are some outliers of course, but also
                                that
                                sometimes, the critics and the users don't agree, for example, if we take a look at the part
                                above the diagonal line (x=y), the user gave a better grade than the critics, and the
                                opposite is true for the bottom part.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartUsersCritics1" class="w-full aspect-square"></div>
                            </div>
                        </div>
                    </div>


                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <h4 class="text-xl font-bold">Rating Difference</h4>
                            <p class="mt-2">
                                Let's define what we're interested in: <b>the rating difference between the critics and the
                                    users</b>.
                            </p>
                            <p class="mt-4">We can see
                                from the following plot that, while this distribution looks normal, it's shifted to the left
                                (as we said
                                before
                                users tend to slightly grade more generously than critics, which means that when making
                                the difference
                                we end up with a negative mean).
                            </p>
                            <p class="mt-4">
                                Running a t-test allows us to affirm that those distributions are normal,
                                and more
                                interestingly, the <u>rating difference is significant</u>. It's worth studying and
                                analyzing it deeper.
                            </p>
                            <p class="mt-4">
                                Even if this first meal is quite quickly prepared, it raises the question we want to answer:
                                <b>what can
                                    explain
                                    this discrepancy?</b>
                            </p>

                            <p class="mt-4">
                                Let's open our favorite cookbook and look for recipes that could help us explain that.
                            </p>

                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartUsersCritics2" class="w-full aspect-square"></div>
                            </div>
                        </div>
                    </div>


                </section>
            </section>

            <section id="cooking-time" class="section text-justify">
                <h2 class="text-4xl lg:text-5xl font-bold mt-8">Time to cook</h2>
                <h5 class="text-xl lg:text-2xl italic text-slate-600 mt-1 ml-1">Exploring the ingredients</h5>

                <!-- ==== COUNTRIES ==== -->
                <section id="countries" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-5 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Countries
                    </h3>
                    <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">A taste of the world</h5>
                    <div class="grid lg:grid-cols-2 mt-3 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Visual Appetizer</h4>
                            <p class="mt-2">
                                In the grand kitchen of our data-driven analysis, let's craft a narrative as we examine the
                                intricate
                                relationship between a movie's country of origin and its critical reception. To whet our
                                appetites for
                                understanding, we must first visually savor the prepared plots—each a dish to be dissected
                                for its unique
                                storytelling flavors.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartCountries1" class="h-full min-h-[700px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <h4 class="text-xl font-bold">Pearson Correlation</h4>
                            <p class="mt-2">
                                The Pearson coefficient provides a more nuanced but raw flavor profile of each country's
                                cinematic output,
                                taking into account only one variable at a time. Each bar, with its confidence interval
                                whiskers,
                                indicates the strength and direction of the relationship between a movie's country of origin
                                and its rating
                                difference. Notice the subtle hints of positive correlations for <i
                                    class="feature">France</i> and <i class="feature">Iran</i>,
                                suggesting that movies
                                from these regions carry a certain <i>je ne sais quoi</i> that resonates with critics. On
                                the flip side,
                                the
                                <i class="feature">United States</i> and <i class="feature">Canada</i> show negative
                                correlations, implying a
                                different critical
                                reception, perhaps due
                                to the commercial seasoning of their movie industries. <i class="feature">French
                                    movies</i>, with a <b>correlation of 0.141</b> and a
                                <b>p-value strikingly close to zero</b>, showcase a strong positive alignment with critic
                                ratings. <i class="feature">Iran</i> follows
                                suit but with a lesser <b>correlation of 0.065</b>, still significant enough to suggest that
                                its movies are
                                savored by critics. The plot also reveals the statistical significance (p-value) of these
                                relationships,
                                emphasizing the reliability of our findings.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartCountries2" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>


                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                            <p class="mt-2">
                                Let's delve deeper into the gourmet guide of global cinema by closely examining the OLS
                                coefficients. This
                                plot refines this relationship by controlling for multiple variables. Here, we see <i
                                    class="feature">Iran</i>'s <b>coefficient
                                    soaring to 7.383</b>, a testament to its movies' critical acclaim when other factors are
                                constant. This
                                is
                                contrasted by the <i class="feature">United States</i>, which sees a
                                <b>negative
                                    coefficient of -5.8119</b>, painting a picture of a
                                cinematic giant whose movies are, perhaps, too rich in mainstream appeal for the critic's
                                more selective
                                taste.Iran's positive coefficient is robust, further validating the country's standing with
                                critics. The
                                negative coefficients for powerhouses like the <i class="feature">United
                                    States</i> and
                                <i class="feature">India</i> are stark, reinforcing the
                                narrative that commercial success is not a guaranteed recipe for critical acclaim. Comparing
                                the OLS coefficient with the
                                Pearson correlation, we note a shift in the order of countries and the magnitude of their
                                influence. For
                                example, while <i class="feature">France</i> tops the Pearson plot, <i
                                    class="feature">Iran</i> takes the lead in the OLS analysis,
                                highlighting how
                                controlling for other variables can change the taste profile of our data dish. Despite
                                slight differences,
                                it appears that critics tend to favor movies that offer a distinct cultural voice, complex
                                narratives, and
                                a strong artistic vision—qualities that are often highlighted in French and Iranian movies.
                                Conversely,
                                industries known for their box office prowess, such as Hollywood and Bollywood, might
                                prioritize elements
                                that ensure commercial success. This industry caters to mass appeal rather than the gourmet
                                tastes of
                                critics.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartCountries3" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Tabs -->
                    <div class="flex flex-col mt-6 w-full">
                        <TabsSection :tabs="countriesTabs" :defaultIndex="5" />
                    </div>
                </section>


                <!-- ==== GENRES ==== -->
                <section id="genres" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Genres
                    </h3>
                    <h5 class="text-lg lg:text-xl italic text-slate-600 text-start"></h5>

                    <!-- Basic Viz -->
                    <div class="grid lg:grid-cols-2 mt-5 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Visual Appetizer</h4>
                            <p class="mt-2 text-justify">
                                We can first try to plot our raw genres. This yields this very… flavorless plot. Indeed,
                                while we can see that factually, <i class="feature">live-actions</i> are rated very harshly
                                by critics, we don't know how significant this is. Other weird things can be seen, such as
                                the
                                <i class="feature">Horse racing</i> genre, having a huge confidence interval, as well as the
                                <i class="feature">World History</i>
                                genre, whose interval spans both sides of the difference.
                            </p>
                            <p class="mt-4">
                                What can be said is that maybe,
                                some expected genres show up in this plot, but they might be a bit diluted in the mass of
                                niche
                                subgenres. Sharpen your knives, we have some <i>Mise en place</i> to do.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartGenres1" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Pearson -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2 text-justify">
                            <div>
                                <h4 class="text-xl font-bold">Pearson Correlation</h4>
                                <p class="mt-2">
                                    The first technique in our cookbook is the beloved Pearson correlation. This lovely tool
                                    allows us to
                                    extract significant genres. Out of 314 genres and subgenres, only <u>61 are
                                        significant</u>
                                    for
                                    our
                                    analysis.
                                </p>
                                <p class="mt-4">
                                    Looking a bit more in detail at this plot, the genres exhibited feel way more concrete
                                    than
                                    before. It's not surprising to see critics liking more <i class="feature">World
                                        cinema</i> or <i class="feature">Art film</i>
                                    categories.
                                    On the other
                                    end of the spectrum, <i class="feature">Action</i> movies and <i
                                        class="feature">Comedy</i> have the support of a wider audience.
                                    Interestingly, we do
                                    see <i class="feature">Gross-out</i> and <i class="feature">Gross-out films</i> both
                                    appear. Why do we see
                                    this kind of genre
                                    twice with
                                    the same
                                    result? And even worse: is there something odd behind our analysis?</p>

                                <p class="mt-4">
                                    While filtering out subgenres would
                                    sound natural, it's often in those small niche genres that the critics' tastes were
                                    hiding. We took the
                                    gambit to keep them at first and filter them later through significance methods if
                                    needed. While
                                    instructive, we have to work a bit more on our data.
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartGenres2" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- OLS -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1 text-justify">
                            <div>
                                <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                                <p class="mt-2">
                                    It occurred that the first OLS showed a very high condition number hinting at the
                                    presence
                                    of
                                    a strong multicollinearity. This threatened the interpretation of the results and
                                    required some VIF
                                    filtering. After filtering according to our cookbook, only 93 features were retained and
                                    passed again
                                    through our OLS.
                                    Finally, applying our
                                    significance threshold (p-value&lt;0.05), the filtered OLS yields about <u>22
                                        significant genres</u>.
                                </p>
                                <p class="mt-4">
                                    Looking closer at our plot, we see that the previously spotted parasitic genres such as
                                    <i class="feature">Gross
                                        out</i> have been correctly filtered out, providing a way cleaner overview of what
                                    genres impact the
                                    rating
                                    difference. For the finest gourmet amongst you, the results give an adjusted R&#178; of
                                    0.136, meaning
                                    that
                                    the genres alone can explain up to <b>13.6%</b> of the variance of the rating difference
                                    between critics
                                    and
                                    users.
                                </p>
                                <p class="mt-4">
                                    However, let's stay down-to-earth. The confidence interval around some of these genres
                                    triggers a small
                                    warning, and for instance, the <i class="feature">Inspirational
                                        Drama</i> or <i class="feature">Feminist Film</i> genres
                                    shouldn't be judged
                                    so fast. This
                                    wide confidence interval can partially be explained by the relatively low number of
                                    movies in those
                                    categories.
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
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

                <!-- ==== AWARDS ==== -->
                <section id="awards" class="section text-justify">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-12 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Awards
                    </h3>
                    <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">The Michelin guide of movies</h5>
                    <!-- Basic Viz -->
                    <div class="grid lg:grid-cols-2 mt-5 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Visual Appetizer</h4>
                            <p class="mt-2">
                                Another ingredient crucial to the success of our recipe is the awards a movie receives. We
                                would like to explore whether the awards the score gap between users and critics.
                                A first sort could allow us to exhibit what types of awards display the biggest differences.
                            </p>
                            <p class="mt-4">
                                This initial plot shows that there can be a divergence between critics' and audiences'
                                perceptions of moives. For movies with prestigious awards, like the <a
                                    href="https://en.wikipedia.org/wiki/Golden_Globe_Awards" target="_blank"
                                    class="feature">Golden Globes</a> or the <a
                                    href="https://en.wikipedia.org/wiki/Academy_Awards" target="_blank"
                                    class="feature">Oscars</a>, critics tend to rate
                                them higher than the audience. Contrarily, critics rated movies that won the <a
                                    href="https://en.wikipedia.org/wiki/Golden_Raspberry_Awards" target="_blank"
                                    class="feature">Golden Raspberry
                                    (Razzie)</a> award much lower than the general audience, which seems consistent with
                                Razzie's intention to highlight movies that are generally considered bad.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartAwards1" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Pearson -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <div>
                                <h4 class="text-xl font-bold">Pearson Correlation</h4>
                                <p class="mt-2">
                                    By running a Pearson correlation on the data, we notice that the <a
                                        href="https://en.wikipedia.org/wiki/National_Board_of_Review" class="feature italic"
                                        target="_blank"> National Board of
                                        Review Award </a> shows the highest positive correlation among the awards, which
                                    suggests that as the number of National Board of Review awards increases, the rating
                                    difference between critics and audiences also tends to increase. The <i
                                        class="feature">Oscar Award</i> also
                                    has a positive correlation, indicating a similar trend as the National Board of Review,
                                    albeit to a lesser extent.
                                    The only one among the listed awards with a negative correlation is the <i
                                        class="feature">Golden Raspberry
                                        Award</i>, suggesting that critics rate these movies lower than audiences do.
                                </p>
                                <p class="mt-4">
                                    So there is generally a positive correlation between the number of awards a movie
                                    receives and the rating difference between critics and audiences, except for the <i
                                        class="feature">Golden
                                        Raspberry Awards</i>. However, the magnitude of these correlations is generally
                                    small (all
                                    below 0.15), indicating that while there is a tendency, it is not strong.
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartAwards2" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- OLS -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <div>
                                <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                                <p class="mt-2">
                                    The initial OLS results show a low condition number (12.7) indicating low
                                    multicollinearity. It is thus not necessary to run VIF and another OLS after.
                                </p>
                                <p class="mt-4">
                                    The OLS results filter down the awards from 8 to <u>5 significant awards</u>.
                                    While the regression model is statistically significant, indicating that there is an
                                    association, it has limited predictive power because of the <b>low R&#178;</b> value
                                    (0.013).
                                    This
                                    means that movie awards are not strong predictors of the difference in ratings between
                                    critics and general audiences on their own: other factors also affect the rating
                                    difference.
                                </p>
                                <p class="mt-4">
                                    The coefficients from the bar chart provide individual estimates of the impact of each
                                    award on the rating difference, with the <i class="feature">National Board of Review
                                        awards</i> showing the
                                    strongest positive impact and the <i class="feature">Razzie awards</i> showing a
                                    negative impact. In the
                                    middle, the <i class="feature">European Film Award</i> shows a positive coefficient,
                                    suggesting a smaller but
                                    still positive effect on the rating difference. The <i class="feature">Oscar Award</i>
                                    also has a positive
                                    coefficient, indicating a positive effect on the rating difference.

                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartAwards3" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <p class="mt-4">
                        In summary, while the regression model is statistically significant, its predictive power is
                        very limited, explaining only a small fraction of the variance in the rating differences.
                        The residuals are not normally distributed, but there seems to be no serious issue with
                        autocorrelation or multicollinearity. The improvement over the baseline is minimal,
                        indicating that while some predictors are significant, their overall impact on the model's
                        predictive accuracy is limited.
                    </p>

                    <!-- Tabs -->
                    <div class="flex flex-col mt-8 w-full gap-5">
                        <TabsSection :tabs="awardsTabs" :defaultIndex="6" />
                    </div>
                </section>


                <section class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-6 mt-12">
                    <div class="flex flex-col">
                        <h3 class="text-3xl lg:text-4xl font-bold items-center text-start">
                            <BookmarkIcon class="w-9 h-9 float-left mr-2" />Hors d'oeuvre
                        </h3>
                        <h5 class="text-lg lg:text-xl italic text-slate-600 text-start mb-4">Tasting Notes on Methodologies
                        </h5>
                        <p>
                            That's a lot to digest so far, so let's have a little break to let it sink in and prepare a
                            little <b>hors-d'oeuvre</b>. We'd like to go into a little bit of detail about our selected
                            “recipes”
                            and
                            discuss them a bit.
                        </p>
                        <p class="mt-4">
                            The <b>Pearson method</b> offers simplicity and a direct taste test of correlation, but it can't
                            account for the complex mix of ingredients that go into movie ratings. It's like tasting a sauce
                            before it's been fully seasoned - useful, but not the complete flavor. Its advantages lie in its
                            straightforward interpretation, but it falls short by not considering other potentially
                            confounding spices.
                        </p>
                        <p class="mt-4">
                            The <b>OLS method</b>, however, simmers down the data to control for various elements, akin to a
                            slow-cooked stew that melds flavors together for a more comprehensive profile. This method
                            allows us to taste the unique contribution of each country, but it can be a complex dish to
                            digest, requiring assumptions like linearity and normality that may not always hold. One
                            drawback is that significant results can be influenced by outliers, just like how a single
                            overpowering spice can skew the taste of a dish. The OLS sensitivity to outliers is the reason
                            that motivates the addition of the VIF filtering to mitigate the threat on the interpretability,
                            but the other assumptions are core to this type of analysis and can't be simply ignored. In a
                            nutshell, we did our best, but take it with a pinch of salt!
                        </p>
                    </div>
                </section>

                <!-- ==== RELEASE YEAR ==== -->
                <section id="release-year" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-12 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Release Year
                    </h3>
                    <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">The older, the better?</h5>
                    <div class="flex flex-col w-full mt-5">
                        <div ref="chartReleaseYear1" class="h-full min-h-[600px] w-full"></div>
                    </div>

                    <div class="flex flex-col w-full">
                        <div ref="chartReleaseYear2" class="h-full min-h-[600px] w-full"></div>
                    </div>

                    <p class="mt-2 text-justify">
                        The first set of plots shows that both the Metascore and IMDb ratings have a general downward
                        trend
                        over the years. This could suggest that movies in general are getting worse, or perhaps more
                        likely,
                        that scoring criteria have become stricter over time. We can also guess that the type of people
                        who
                        are rating old movies are probably old movie amateurs, and it is important to note that the
                        rating
                        doesn't reflect the popularity when the movie was released, but nowadays!
                    </p>
                    <p class="mt-4">
                        The plot for rating differences over the years indicates that the gap between Metascore and IMDb
                        ratings has generally been widening. We can note that the average metascore felt way more than
                        the
                        IMDb rating, as it went from more than 90 for the 1920 movies, to around 55 for the 2010 movies,
                        meanwhile, the IMDb rating fell from 80 to around 65. Early in the data, Metascore ratings were
                        higher than IMDb, and over time, this trend reversed.
                    </p>

                    <h4 class="text-xl font-bold mt-4">Pearson Correlation</h4>
                    <p class="mt-2">
                        Running Pearson correlation gives us some values. We especially find a negative correlation of
                        <b>-0.201596</b>. It indicates that increasing the year will decrease the rating difference, which
                        seems
                        normal if we take a look at the trend explained before. The absolute value is nevertheless not
                        big,
                        so it is <b>not a super strong correlation</b>. The very small p-value indicates that the obtained
                        value is
                        <u>statistically significant</u>.
                    </p>

                    <h4 class="text-xl font-bold mt-4">Ordinary Least Squares (OLS)</h4>
                    <p class="mt-2">
                        Running the OLS also gives numbers, indicating big multicollinearity, which seems normal as
                        years
                        are strongly related. We also find a negative coefficient for years of <b>-0.19</b>, indicating
                        that
                        with
                        each passing year, the rating difference decreases by 0.19 points, and thus by 1.9 points every
                        decade. We also learned using the
                        R&#178; value that the year explains
                        about <b>4.1%</b> of the variance in rating difference, which is not a lot but still
                        <u>significant</u>.
                    </p>
                </section>

                <!-- ==== ACTORS ==== -->
                <section id="actors" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-12 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Actors
                    </h3>
                    <!-- Pearson -->
                    <div class="grid lg:grid-cols-2 mt-5 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <div>
                                <h4 class="text-xl font-bold">Pearson Correlation</h4>
                                <p class="mt-2 text-justify">
                                    Once again, a rotten tomato could spoil the real taste of the preparation, and we want
                                    to avoid such
                                    mistakes. Cleaning our ingredient basket with the Pearson correlation gives this yummy
                                    plot of <u>426
                                        significant</u> actors out of 3151 ones.
                                </p>
                                <p class="text-justify mt-4">
                                    Let's look a bit more in detail at what this shows us. Analyzing the significant actors
                                    already gives
                                    quite interesting results. We can notice that the best-performing actors for impressing
                                    critics are
                                    mostly
                                    old actors, such as <i class="feature">Cary Grant</i> or <i class="feature">Ward
                                        Bond</i>. A small warning here: since those
                                    actors are mostly
                                    from the
                                    beginning of cinema history, their results might be biased. Indeed, it is possible that
                                    their less
                                    renowned movies or less-performing roles were simply filtered out due to the lack of
                                    data. Indeed, a
                                    movie
                                    too old might not even be rated retrospectively by critics and users if it was a
                                    forgettable experience.
                                    This phenomenon could bias them toward higher scores. This is also to be mitigated by
                                    the fact that, in
                                    a
                                    way, if those actors are still known to experts, they marked cinema history and could
                                    deserve their
                                    place.
                                </p>
                                <p class="text-justify mt-4">
                                    On the other hand, recent movies and actors are much less likely to be given the chance
                                    to not be scored
                                    badly for a bad movie. No second chances for <i class="feature">Ryan
                                        Reynolds</i> or
                                    <i class="feature">Ashton Kutcher</i>. Indeed, alternating between
                                    deep roles highlighting their talent and lighter characters might be detrimental to them
                                    in this plot.
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartActors1" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- OLS -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1 text-justify">
                            <div>
                                <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                                <p class="mt-2 ">
                                    Running the OLS gives once more insightful results, with an adjusted R&#178; of 0.13
                                    (<b>13%</b>).
                                    Having
                                    specific actors
                                    seems then to be impactful on the results, with the <u>20 significant</u> ones shown in
                                    this plot.
                                </p>
                                <p class="mt-4">Once
                                    again, the variances are quite big, probably due to the relatively low number of movies
                                    each actor's been
                                    in compared to the total number of movies and actors. A final remark must be noted too:
                                    we can't be sure
                                    that the genres and the actors are not entangled in a way. Some actors are probably
                                    performing well in
                                    specific genres while being considered awful in others. Sadly, we've been unable to
                                    completely rule out
                                    that kind of confounding effect, since all of the features we have are of course
                                    strongly
                                    interconnected.
                                </p>
                                <p class="mt-4">
                                    Comparing the results of Pearson shows that the results seem comparable, with some
                                    slight differences
                                    in order. The type of the actors, however, seems quite consistent between the two.
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
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

                <!-- ==== TROPES ==== -->
                <section id="tropes" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-12 items-center text-start mb-4">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Tropes
                    </h3>
                    <p>
                        The last ingredient for our glorious meal is the tropes. As a friendly reminder, tropes are “a
                        significant
                        or recurrent theme; a motif”. Maybe this boring repetitive structure in this site was an artistic
                        choice from
                        the beginning. Let's get back to the kitchen. Because tropes are categories that are human-made and
                        manually
                        assigned to each movie on the internet, the classification can be even messier than movie genres.
                        But since
                        it is born from the human need for categorization, we do think it can be a very valuable source of
                        information.
                    </p>
                    <p class="mt-4">
                        Notice that, while the dataset merging in the previous steps didn't leave out a lot of movies, the
                        tropes
                        merging drastically reduced the number of data points, down to approximately 2495, as mentioned
                        during our
                        fridge inspection. Still plenty of room to work with! We know you're already drooling, but hold on
                        through
                        this last step!
                    </p>

                    <!-- Pearson -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-2">
                            <h4 class="text-xl font-bold">Pearson Correlation</h4>
                            <p class="mt-2 text-justify">
                                As expected, the Pearson correlation filtered out our movies down to around <u>300
                                    significant tropes</u>,
                                which
                                is indeed enough to continue our analysis. Diving into the plot, we can see funny and
                                odd tropes
                                standing out. What is great is that the <i class="feature">Oscar Bait</i>
                                type of movie, with a <b>correlation of 0.1</b>, is taking the highest place of the plot,
                                meaning that indeed, this trope is a
                                significant indicator
                                for critical reception. On the other end, <i class="feature">Ms
                                    Fanservice</i>, with a <b>correlation of 0.11</b>, indicates that... fans like it. So
                                far so good. This is no real surprise since these qualifiers could have
                                been attributed
                                a posteriori. In general, we can suspect that these tropes are tightly related to all other
                                features like
                                <i class="feature">Deliberately Monochrome</i> is way more likely to
                                qualify as <i class="feature">Art Film</i> and is likely to be considered part of
                                <i class="feature">Auteur license</i> too. On the other hand, expected tropes binded with
                                the genre, like <i class="feature">Slasher</i> reappears,
                                reinforcing the insights provided by the Genre analysis. In general, the confidence
                                intervals are wide,
                                but quite constant over the sample. However, the most precise tropes standing out might be a
                                bit harder to
                                interpret. Furthermore, we do see that the <i class="feature">Magical
                                    something</i>
                                trope appears twice, and referring to the
                                methods we used, we could expect high multicollinearity.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-1 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartTropes1" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <!-- OLS -->
                    <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1">
                            <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                            <p class="mt-2 text-justify">
                                By running our first OLS, we get as expected a high condition number implying a high
                                multicollinearity. By
                                applying VIF filtering we cut out almost 20 tropes, leaving us now with 315 features. The
                                OLS regression
                                can now be performed with the hopes of better results. With an impressive <b>adjusted
                                    R&#178; of 0.2</b>
                                and <u>36
                                    significant tropes</u>, the OLS shows very encouraging numbers. However, visualizing
                                what's the outcome
                                in our
                                now classic plot can be a little bit disturbing. Instead of cleaning out obscure tropes, the
                                outcome is
                                even harder to interpret. Based on the metrics evaluating the regression quality, the
                                results are good,
                                but here we're probably limited by our projections. These results could've been expected
                                since most
                                of them are heavily tailored and strongly related to the movie's target audience. However,
                                we do observe
                                wider confidence intervals, giving us an insight that maybe, the variance of these rating
                                differences is
                                high. Let's still highlight the fact that <i class="feature">Roof
                                    hopping</i> performs
                                well to impress critics, while strangely,
                                movies like Mary Poppins and The Matrix are both part of this category. If you're curious to
                                know what a
                                trope means, play around our <a href="#playground" class="underline">playground</a>
                                at the end,
                                and don't hesitate to learn using the source of our
                                tropes data, <a href="https://tvtropes.org" target="_blank"
                                    class="text-red-900 underline hover:text-red-400">tvtropes.org</a>.
                            </p>
                        </div>
                        <div class="flex flex-col order-2 lg:order-2 w-full">
                            <div class="flex flex-col h-full w-full">
                                <div ref="chartTropes2" class="h-full min-h-[600px] w-full"></div>
                            </div>
                        </div>
                    </div>

                    <div class="flex flex-col mt-8 w-full gap-5">
                        <TabsSection :tabs="tropesTabs" :defaultIndex="3" />
                    </div>
                </section>
            </section>

            <section id="conclusion" class="section text-justify">
                <h2 class="text-4xl lg:text-5xl font-bold mt-16">Conclusion</h2>
                <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">Mixing it all with a yummy conclusion</h5>
                <p class="mt-2 text-justify">
                    Now that all of our ingredients are selected and refined, we’d like to see if mixing them can enhance
                    the results we obtain. Let’s first recall the results we obtained for the most important of our metrics,
                    the adjusted R&#178;:
                </p>

                <!-- Vertical Table -->
                <div class="block lg:hidden mt-4">
                    <div class="flex flex-col border-b drop-shadow-xl rounded overflow-hidden">
                        <div class="flex justify-between px-3 py-2 bg-slate-600 font-bold text-white">
                            <div>Feature</div>
                            <div>Adj. R²</div>
                        </div>
                        <div class="flex justify-between px-3 py-2 bg-slate-100">
                            <div>Genres</div>
                            <div>0.135</div>
                        </div>
                        <div class="flex justify-between px-3 py-2 bg-slate-200">
                            <div>Actors</div>
                            <div>0.130</div>
                        </div>
                        <div class="flex justify-between px-3 py-2 bg-slate-100">
                            <div>Release data</div>
                            <div>0.041</div>
                        </div>
                        <div class="flex justify-between px-3 py-2 bg-slate-200">
                            <div>Countries</div>
                            <div>0.059</div>
                        </div>
                        <div class="flex justify-between px-3 py-2 bg-slate-100">
                            <div>Awards</div>
                            <div>0.013</div>
                        </div>
                        <div class="flex justify-between p-2 bg-slate-200">
                            <div>Tropes</div>
                            <div>0.198</div>
                        </div>
                    </div>
                </div>

                <table class="hidden lg:table w-full border-slate-600 drop-shadow-lg mt-4 rounded overflow-hidden">
                    <thead>
                        <tr class="border-slate-600 border-b-[1px] bg-slate-600 text-white text-center lg:text-start">
                            <th class="text-end p-1 pr-2 ">Feature</th>
                            <td>Genres</td>
                            <td>Actors</td>
                            <td>Release date</td>
                            <td>Countries</td>
                            <td>Awards</td>
                            <td>Tropes</td>
                        </tr>
                    </thead>

                    <tbody>
                        <tr class="bg-slate-100">
                            <th class="text-end p-1 pr-2">Adj. R&#178;</th>
                            <td>0.135</td>
                            <td>0.130</td>
                            <td>0.041</td>
                            <td>0.059</td>
                            <td>0.013</td>
                            <td>0.198</td>
                        </tr>
                    </tbody>
                </table>
                <p class="mt-4">
                    The <b>tropes</b> were indeed the most performant indicator we prepared so far but were also a bit
                    obscure and
                    hard to interpret. The <b>genres</b> and <b>actors</b> are very good indicators overall. The
                    awards are quite interesting too, despite their low R&#178;, since they were only 5 significant awards.
                    The <b>release
                        year</b> is a
                    single continuous indicator with respectable results, and the <b>countries</b> might also be very good,
                    accounting for almost 6% of the variance explained. However, these metrics account for each feature
                    independently.
                </p>
                <p class="mt-4">
                    Gathering all of the mise en place from before, we keep <u>88 significant features</u> that we
                    want to use. We now want to perform a last blend, extracting the most out of it and hoping the results
                    are even more interesting!
                </p>

                <!-- Pearson -->
                <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                    <div class="flex flex-col order-1 lg:order-2">
                        <h4 class="text-xl font-bold">Pearson Correlation</h4>
                        <p class="mt-2 text-justify">
                            Looking at the type of significant features kept by Pearson, we see that interestingly, the
                            Award and Country indeed appear in the rating. We observe that <u>65 features are considered
                                significant</u> (out of 88) by the Pearson test. Let's look at the type of features: 10
                            genres, 2 awards,
                            4 tropes, 1 country, and 1 actor, as well as the year appearing in the top 20. Let's break
                            it down.</p>
                        <p class="mt-4">
                            The blockbuster weight of the <i class="feature">USA</i> can easily explain why they appear
                            here. The genre
                            seems to be a predominant indicator, as could be expected from the specific analysis showing
                            how polarizing they are. <i class="feature">Drama</i> and <i class="feature">Black & White</i>
                            again take the lead on the critic side, and <i class="feature">Action</i> and
                            <i class="feature">Slapstick</i> are again kicking in for users.
                        </p>

                        <p class="mt-4">
                            The only actor appearing and worth mentioning is <i class="feature">Gerard
                                Butler</i>, who was not even in the top 20 of the specific Actor analysis but appears here.
                            This can
                            be explained maybe by his roles in a lot of movies appreciated more by users, from very good
                            ones
                            (<i>How to Train your Dragon</i>) to mediocre ones (<i>Movie 43</i>). The only movie he starred
                            in that is
                            favored by the critics is <i>Coriolanus</i>, a movie adaptation of Shakespeare's piece.
                        </p>
                        <p class="mt-4">Other than
                            that, not much is unexpected so far, and the overall robustness of the analysis is strengthened
                            by the relatively constant confidence intervals, maybe a bit wide for our liking but overall in
                            a manageable range.
                        </p>
                    </div>
                    <div class="flex flex-col order-2 lg:order-1 w-full">
                        <div class="flex flex-col h-full w-full">
                            <div ref="chartGlobal1" class="h-full min-h-[600px] w-full"></div>
                        </div>
                    </div>
                </div>

                <!-- OLS -->
                <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
                    <div class="flex flex-col order-1 lg:order-1">
                        <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                        <p class="mt-2 text-justify">
                            Sadly, some of our features were again seemingly multicollinear, and the VIF filtering brings
                            them down to 81 significant ones to be fed to our OLS. Poor Gerard Butler didn't survive the
                            filtering, as well as the United States. There are <u>14 significant features</u> according to
                            the OLS (out of 81), and in
                            detail, we do see only Genre, and Tropes type of features. While consistent with the specific
                            analysis, i.e. the orientation of their influence is the same, we feel like something is missing
                            in that final result.
                        </p>
                        <p class="mt-4">
                            Looking back at our summary table, Genres and Tropes are indeed the two
                            highest adj. R&#178; scores, and it's thus no real surprise to see them dominate there. But it
                            feels
                            like we're losing a lot of precious information there, maybe because the Genres and Tropes are
                            overwhelming the overall analysis. But looking at the statistical metrics, the results are
                            nevertheless impressive: the adjusted R&#178; is now at <b>0.231</b>, which is a significant
                            boost based on
                            what we had before. Other model indicators tend to show that the results are better. In the end,
                            it seems that using only a few tropes and a few genres could allow us to explain a significant
                            part of the variance.
                        </p>
                    </div>
                    <div class="flex flex-col order-2 lg:order-2 w-full">
                        <div class="flex flex-col h-full w-full">
                            <div ref="chartGlobal2" class="h-full min-h-[600px] w-full"></div>
                        </div>
                    </div>
                </div>
                <p class="mt-4 my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4 ">
                    This result of only <b>23% of explained variance</b> might seem low, but since this kind of modeling is
                    really
                    hard, involving features <b>highly correlated together</b>, a human dimension hard to grasp, and other
                    facts that are simply not described by the features we had at our disposal, we can be pretty
                    satisfied with the overall dish concocted there. What's great is that our careful methodology
                    and feature selection indeed allowed us to improve the results of the model, showing both an
                    insightful Pearson plot and an interesting OLS.
                </p>

                <section id="next" class="section">
                    <h3 class="text-3xl lg:text-4xl font-bold mt-5 items-center text-start">
                        <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />What's next?
                    </h3>
                    <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">Dessert is served, but we're still
                        hungry</h5>

                    <div class="grid lg:grid-cols-3 mt-3 w-full gap-5">
                        <div class="flex flex-col order-1 lg:order-1 col-span-2">
                            <p>
                                To go further, we'd be honored to let future
                                chefs add their spices to the meal. We thought about exploring those topics too:
                            <ul class="list-disc list-inside pl-5">
                                <li>Exploring the difference between the critics themselves, since they're not grading the
                                    same
                                    way,
                                    depending on the genre of movies for instance.
                                </li>
                                <li>
                                    Try to unveil the way the Metascore is weighted and computed, and why not, develop a
                                    metric
                                    to
                                    find a publisher to read based on your taste?</li>
                                <li>
                                    Find a way to cluster users based on the score they give, be it according to the genres
                                    or
                                    another type of features</li>
                                <li>
                                    Explore interaction terms between the features we extracted</li>
                            </ul>
                            </p>
                            <p class="mt-4">
                                We do hope that this dish could satisfy any Anton Ego, but in case you have room for more,
                                don't hesitate to taste <a target="_blank" class="underline"
                                    href="https://github.com/orgs/epfl-ada/repositories">other projects</a> made by the ADA
                                teams through the years.

                            </p>
                        </div>
                        <div
                            class="flex flex-col col-span-3 order-2 lg:col-span-1 lg:order-2 w-full items-center justify-center">
                            <div class="flex flex-col h-full w-full items-center justify-center">
                                <img src="/ego.png" alt="ego"
                                    class="lg:w-full mt-4 drop-shadow-xl max-h-[400px] lg:max-h-none hover:scale-y-105 hover:-scale-x-105 hover:drop-shadow-none transition duration-300 -scale-x-100" />
                            </div>
                        </div>
                    </div>
                </section>


            </section>

            <section id="playground" class="section">
                <h2 class="text-4xl lg:text-5xl font-bold mt-8">The Kitchen</h2>
                <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">Play with our ingredients</h5>
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

.feature {
    @apply text-red-800 font-semibold;
}

.tab-panel {
    width: 100%;
    /* Ensure the panel has a specific width */
    transition: transform 0.6s, opacity 0.6s;
    transform-style: preserve-3d;
    position: relative;
    overflow: hidden;
    backface-visibility: hidden;
}

.tab-enter-active,
.tab-leave-active {
    transition: transform 1s, opacity .5s;
}

.tab-enter-from,
.tab-leave-to {
    transform: rotateY(180deg);
    transform-origin: 0% 0%;
    /* Rotate around the left edge */
    opacity: 0;
}

.tab-leave-from,
.tab-enter-to {
    transform: rotateY(0deg);
    transform-origin: 0% 0%;
    /* Rotate around the left edge */
    opacity: 1;
}
</style>
  
  
  
<script setup>
import { onMounted, ref, defineAsyncComponent, defineComponent } from 'vue';
import { BookmarkIcon } from "@heroicons/vue/24/solid"
import { TabGroup, TabList, Tab, TabPanels, TabPanel, TransitionRoot, TransitionChild } from '@headlessui/vue'
import * as plotFunctions from './plots.js'
import MathJaxEquation from './MathJaxEquation.vue';
const BASE_URL = import.meta.env.VITE_BASE_URL;


const Playground = defineAsyncComponent(() => import('./Playground.vue'));
const TabsSection = defineAsyncComponent(() => import('./TabsSection.vue'));

const activeCookbookTabId = ref(0);

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
const chartReleaseYear1 = ref(null);
const chartReleaseYear2 = ref(null);
const chartTropes1 = ref(null);
const chartTropes2 = ref(null);
const chartGlobal1 = ref(null)
const chartGlobal2 = ref(null)

const countriesTabs = ref(null)
const genresTabs = ref(null)
const awardsTabs = ref(null)
const tropesTabs = ref(null)
const actorsTabs = ref(null)

const fetchData = async (path) => {
    const originUrl = window.location.origin;
    if (BASE_URL && BASE_URL !== '/') return await fetch(`${originUrl}/${BASE_URL}/${path}`).then(response => response.json());
    return await fetch(`${originUrl}/${path}`).then(response => response.json());
};


onMounted(async () => {

    const movies = await fetchData('/data/playground-movies.json');

    // == TABS WIDGETS == //
    fetchData('/data/countriesTabs.json').then(data => {
        countriesTabs.value = data;
    });
    fetchData('/data/genresTabs.json').then(data => {
        genresTabs.value = data;
    });
    fetchData('/data/awardsTabs.json').then(data => {
        awardsTabs.value = data;
    });
    fetchData('/data/tropesTabs.json').then(data => {
        tropesTabs.value = data;
    });
    fetchData('/data/actorsTabs.json').then(data => {
        actorsTabs.value = data;
    });

    // == CHARTS == //
    // Users Bar Chart
    if (chartUsers) {
        plotFunctions.callbackUser(movies, chartUsers)
    }

    // Metascore Bar Chart 
    if (chartMetascore) {
        plotFunctions.callbackMetascore(movies, chartMetascore)
    }

    // Users vs Critics Scatter
    if (chartUsersCritics1) {
        plotFunctions.callbackUsersCritics1(movies, chartUsersCritics1)
    }

    // User vs Critics 2
    if (chartUsersCritics2) {
        plotFunctions.callbackUsersCritics2(movies, chartUsersCritics2)
    }


    // Countries 1
    if (chartCountries1) {
        plotFunctions.callbackCountries1(chartCountries1, "/data/countries-1.json")
    }

    // Countries 2
    if (chartCountries2) {
        plotFunctions.callbackCountries2(chartCountries2, "/data/countries-2.json")
    }

    // Countries 3
    if (chartCountries3) {
        plotFunctions.callbackCountries3(chartCountries3, "/data/countries-3.json")
    }


    // Genres 1
    if (chartGenres1) {
        plotFunctions.callbackGenres1(chartGenres1, "/data/genres-1.json")
    }

    // Genres 2
    if (chartGenres2) {
        plotFunctions.callbackGenres2(chartGenres2, "/data/genres-2.json")
    }

    // Genres 3
    if (chartGenres3) {
        plotFunctions.callbackGenres3(chartGenres3, "/data/genres-3.json")
    }

    // Awards 1
    if (chartAwards1) {
        plotFunctions.callbackAwards1(chartAwards1, "/data/awards-1.json")
    }

    // Awards 2
    if (chartAwards2) {
        plotFunctions.callbackAwards2(chartAwards2, "/data/awards-2.json")
    }

    // Awards 3
    if (chartAwards3) {
        plotFunctions.callbackAwards3(chartAwards3, "/data/awards-3.json")
    }

    // Actors 1
    if (chartActors1) {
        plotFunctions.callbackActors1(chartActors1, "/data/actors-1.json")
    }

    // Actors 2
    if (chartActors2) {
        plotFunctions.callbackActors2(chartActors2, "/data/actors-2.json")
    }

    // Release Year
    if (chartReleaseYear1) {
        plotFunctions.callbackReleaseYear(chartReleaseYear1, chartReleaseYear2, "/data/releasedate.json")
    }


    // Tropes 1
    if (chartTropes1) {
        plotFunctions.callbackTropes1(chartTropes1, "/data/tropes-1.json")
    }

    // Tropes 2
    if (chartTropes2) {
        plotFunctions.callbackTropes2(chartTropes2, "/data/tropes-2.json")
    }


    // Global 1
    if (chartGlobal1) {
        plotFunctions.callbackGlobal1(chartGlobal1, "/data/global-1.json")
    }

    // Global 2
    if (chartGlobal2) {
        plotFunctions.callbackGlobal2(chartGlobal2, "/data/global-2.json")
    }

});

</script>