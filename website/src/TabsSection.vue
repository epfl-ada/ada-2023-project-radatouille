<template>
    <TabGroup as="div" class="flex z-[2] w-full">
        <TabList as="div" class="flex flex-col p-3 space-x-1 rounded-xl bg-gradient-to-t to-[#67001f] from-[#f6e8c3]">
            <Tab
                as="button"
                v-for="(tab, index) in tabs"
                :key="tab.id"
                class="w-full py-2.5 text-xs lg:text-sm leading-5 font-medium text-white drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] rounded-lg focus:outline-none focus:ring-2 ring-offset-2 ring-offset-red-700 ring-white ring-opacity-60"
                :class="{ 'bg-slate-200 border-l-4 border-red-700 font-bold !text-black drop-shadow-none': tab.id === activeTabId }" @click="activeTabId = tab.id"
                >
                {{ tab.name }}
            </Tab>
        </TabList>
        <TabPanels as="div" class="ml-5 p-5 bg-slate-200 rounded-xl flex w-full">
            <!-- Tab content -->
            <TabPanel v-for="tab in tabs" :key="tab.id" as="div" class="flex flex-col h-full">
                <img
                v-if="tab.image"
                :src="tab.image"
                class="w-full max-w-xs rounded-lg object-cover object-center mb-4"
                :class="tab.image_aspect == 'square' ? 'aspect-square': null"
                
                >
                <h5 class="text-xl font-semibold mb-1">{{ tab.title }}</h5>
                <p>{{ tab.content }}</p>
                <h6 v-if="tab.movies" class="text-lg font-semibold mb-1 mt-3">Some movies</h6>
                <ul class="list-disc list-inside">
                    <li v-for="item in tab.movies" :key="item">{{ item }}</li>
                </ul>
                <a v-if="tab.link" target="_blank" :href="tab.link" class="bg-slate-800 p-2 text-white rounded-lg font-semibold hover:underline mt-auto ml-auto">See more</a>
            </TabPanel>
        </TabPanels>
    </TabGroup>
</template>

<script setup>
import { ref } from 'vue'
import { Tab, TabGroup, TabList, TabPanels, TabPanel } from '@headlessui/vue';

const props = defineProps({
  tabs: {
    type: Array,
    default: () => []
  }
});


const activeTabId = ref(props.tabs.length > 0 ? props.tabs[0].id : null);

</script>