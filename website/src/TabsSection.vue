<template>
    <TabGroup v-if="tabs && tabs.length > 0" as="div" class="flex flex-col lg:flex-row z-[2] w-full" :default-index="defaultIndex">
        <button ref="buttonRef" class="lg:hidden py-3 px-4 rounded-xl bg-gradient-to-r to-[#67001f] from-[#f6e8c3] mb-3 flex"
            :show="!isTabListVisible" @click="isTabListVisible = !isTabListVisible">
            <span class="text-white drop-shadow-[0_1.5px_3px_rgba(0,0,0,1)] font-semibold">Menu</span>
            <Bars3Icon class="ml-auto w-6 h-6 text-white" />
        </button>
        <TransitionRoot as="template" :show="isTabListVisible" v-if="isMobileView">
            <FloatingDialog :isOpen="isTabListVisible" :anchorEl="buttonRef" @close="isTabListVisible = false" class="w-full">
                <div class="min-h-screen px-4 text-center">
                    <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0"
                        enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                        <div class="fixed inset-0 bg-black bg-opacity-25" aria-hidden="true" @click="isTabListVisible = false"></div>
                    </TransitionChild>

                    <!-- This element is to trick the browser into centering the modal contents. -->
                    <span class="inline-block h-screen align-middle" aria-hidden="true">&#8203;</span>
                    <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 scale-95"
                        enter-to="opacity-100 scale-100" leave="ease-in duration-200" leave-from="opacity-100 scale-100"
                        leave-to="opacity-0 scale-95">
                        <div
                            class="inline-block w-full max-w-md p-6 my-8 overflow-hidden text-left align-middle transition-all transform bg-white shadow-xl rounded-2xl">
                            <TabList as="div"
                                class="flex lg:hidden flex-col p-3 mt-5 space-x-1 rounded-xl bg-gradient-to-t to-[#67001f] from-[#f6e8c3]">
                                <Tab as="button" v-for="(tab, index) in tabs" :key="index"
                                    class="w-full py-2.5 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none focus:ring-2 ring-offset-2 ring-offset-red-700 ring-white ring-opacity-60"
                                    :class="{ 'bg-slate-200 border-l-4 border-red-700 font-bold !text-black drop-shadow-lg': index === activeTabId }"
                                    @click="() => { activeTabId = index; isTabListVisible = false }">
                                    {{ tab.name }}
                                </Tab>
                            </TabList>
                            <button class="absolute top-0 right-0 mt-4 mr-4" @click="isTabListVisible = false">
                                <XMarkIcon class="w-6 h-6 text-gray-900" />
                            </button>
                        </div>
                    </TransitionChild>
                </div>
            </FloatingDialog>
        </TransitionRoot>
        <TabList as="div" v-if="!isMobileView"
            class="hidden lg:flex flex-col py-3 px-4 space-x-1 rounded-xl bg-gradient-to-t to-[#67001f] from-[#f6e8c3] shadow-xl">
            <Tab as="button" v-for="(tab, index) in tabs" :key="index"
                class="w-full py-2.5 px-2 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none border-l-4 border-transparent ring-2 ring-offset-2 ring-offset-transparent focus:ring-offset-red-700 ring-transparent ring-opacity-60"
                :class="{ 'bg-slate-200 border-l-4 !border-red-700 font-bold !text-black drop-shadow-lg': index === activeTabId }"
                @click="() => { activeTabId = index; isTabListVisible = false; }">
                {{ tab.name }}
            </Tab>
        </TabList>
        <TabPanels as="div" class="lg:ml-5 p-5 bg-slate-200 rounded-xl flex w-full lg:max-w-md overflow-hidden shadow-xl " >
            <TabPanel v-for="(tab, index) in tabs" :key="index" as="div" class="flex h-full w-full">
                <TransitionRoot :show="activeTabId == index" enter="tab-enter" enter-to="tab-enter-to"
                    enter-from="tab-enter-from" leave="tab-leave" leave-to="tab-leave-to" leave-from="tab-leave-from">
                    <div class="flex flex-col h-full p-1 lg:p-3 tab-content">
                        <!-- Panel Content -->
                        <img v-if="tab.image" :src="tab.image" class="w-full rounded-lg object-cover mb-4"
                            :class="((tab.image_aspect == 'square') ? 'aspect-square' : null) + ' ' + ((tab.image_position == 'top') ? 'object-top' : 'object-center')">
                        <h5 class="text-xl font-semibold mb-1">{{ tab.title }}</h5>
                        <p class="mb-3" v-html="tab.content"></p>
                        <h6 v-if="tab.movies" class="text-lg font-semibold mb-1 mt-3">Some movies</h6>
                        <ul class="list-disc list-inside mb-3">
                            <li v-for="(item, movie_index) in tab.movies" :key="movie_index"><a :href="item.link" target="_blank">{{ item.title }}</a></li>
                        </ul>
                        <a v-if="tab.link" target="_blank" :href="tab.link"
                            class="bg-slate-800 p-2 text-white rounded-lg font-semibold hover:underline mt-auto ml-auto">See
                            more</a>
                    </div>
                </TransitionRoot>
            </TabPanel>
        </TabPanels>
    </TabGroup>
</template>

<style>
/* Define the entering and leaving animations */
.tab-enter,
.tab-leave {
    transition: all 0.4s ease;
}

.tab-enter-from,
.tab-leave-to {
    transform: scale(0.7);
    opacity: 0;
}

.tab-leave-from,
.tab-enter-to {
    transform: scale(1);
    opacity: 1;
}

.tab-content p a, .tab-content ul li a {
    text-decoration: underline;
    color: #67001f;
}

.tab-content p a:hover, .tab-content ul li a:hover {
    color: #a86f80;
    cursor: pointer;
}
</style>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Tab, TabGroup, TabList, TabPanels, TabPanel, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/solid';
import FloatingDialog from './FloatingDialog.vue';

const props = defineProps({
    tabs: {
        type: Array,
        default: () => null
    },
    defaultIndex: {
        type: Number,
        default: 0
    }
});

const activeTabId = ref(null);
const isTabListVisible = ref(false);
const isMobileView = ref(window.innerWidth < 1024);
const buttonRef = ref(null);

const preloadImages = (tabs) => {
    if (!tabs) return;
    tabs.forEach(tab => {
        if (tab.image) {
            const img = new Image();
            img.src = tab.image;

            // Optionally set a low priority to these requests
            //img.setAttribute('loading', 'lazy');
        }
    });
};


const updateWindowSize = () => {
    isMobileView.value = window.innerWidth < 1024;
};

onMounted(() => {
    window.addEventListener('resize', updateWindowSize);
});

onUnmounted(() => {
    preloadImages(props.tabs);
    window.removeEventListener('resize', updateWindowSize);
});

watch(() => props.tabs, (newTabs) => {
    preloadImages(newTabs);
    if (newTabs && newTabs.length > 0) {
        activeTabId.value = props.defaultIndex;
    }
}, { immediate: true });


</script>