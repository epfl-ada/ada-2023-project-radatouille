<template>
    <nav class="max-h-[110px]  lg:max-h-16 flex bg-dark text-light items-center justify-between sticky top-0 left-0 w-full z-10">
        <img src="/remy_silhouette.png" alt="Remy's silhouette" class="w-16 h-16 ml-3 lg:w-12 lg:h-12 lg:ml-5" />
        <div class="flex flex-col px-5 py-10 mx-auto text-center">
            <h1 class="text-lg lg:text-xl font-bold">Screen Tastes: The User-Critic Divide in Cinema</h1>
            <h6 class="text-xs italic text-slate-300">Served by team rADAtouille</h6>
        </div>
        <button class="cursor-pointer w-14 h-14 flex items-center justify-center " title="Open menu"
        @click="toggleMenu" ref="buttonRef">
            <span class="hover:bg-white/90 hover:text-dark rounded-full p-2">
                <Bars3Icon class="w-6 h-6 " />
            </span>
        </button>
    </nav>

    <!-- Mobile menu -->
    <TransitionRoot appear :show="isMobileMenuOpen" as="template">
        <FloatingDialog :isOpen="isMobileMenuOpen" :anchorEl="buttonRef" @close="handleDialogClose">
                <TransitionChild as="template" enter="duration-200 ease-out" enter-from="opacity-0 translate-x-full"
                    enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100"
                    leave-to="opacity-0 translate-x-full">
                    <div class="fixed inset-y-0 right-0 max-w-full flex">
                        <div class="bg-dark text-light h-full w-full overflow-y-auto p-8">
                            <button class="bg-slate-500 rounded-full p-3 text-white fixed top-8 right-8 hover:bg-slate-600"
                                title="Close menu" @click="setIsMobileMenuOpen(false)">
                                <XMarkIcon class="w-6 h-6" />
                            </button>

                            <div v-for="section in sections" :key="section.id" class="mt-4">
                                <h3 class="text-3xl font-medium mt-4">
                                    <a class="flex gap-3 items-center py-2 hover:text-slate-400"
                                        :href="section.mainMenuLink?.link" @click="setIsMobileMenuOpen(false)">
                                        <span>{{ section.mainMenuLink?.title }}</span>
                                        <ChevronRightIcon class="w-6 h-6" />
                                    </a>
                                </h3>
                                <a v-for="link in section.secondaryMenuLinks" :key="link.id"
                                    class="text-xl block py-2 hover:text-slate-400" :href="link.link"
                                    @click="setIsMobileMenuOpen(false)">
                                    {{ link.title }}
                                </a>
                            </div>
                        </div>
                    </div>

                </TransitionChild>

        </FloatingDialog>
    </TransitionRoot>
</template>
  
<script setup>
import {
    TransitionRoot,
    TransitionChild
} from '@headlessui/vue'

import { Bars3Icon, ChevronRightIcon, XMarkIcon } from '@heroicons/vue/24/solid'
import { ref, onMounted, onUnmounted } from 'vue'
import FloatingDialog from './FloatingDialog.vue';

const isMobileMenuOpen = ref(false)
const buttonRef = ref(null);


function toggleMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
}

function handleDialogClose() {
  isMobileMenuOpen.value = false; // Close the dialog
}
const sections = [{
    id: 1,
    mainMenuLink: {
        title: 'Introduction',
        link: '#introduction'
    },
    secondaryMenuLinks: [{
        id: 1,
        title: "What's in our fridge",
        link: '#fridge'
    },
    {
        id: 2,
        title: 'Statistics Cookbook',
        link: '#cookbook'
    }, {
        id: 3,
        title: "Instantaneous Noodles and T-Taste",
        link: '#noodles'
    }
    ]
},
{
    id: 2,
    mainMenuLink: {
        title: 'Time to cook',
        link: '#cooking-time'
    },
    secondaryMenuLinks: [{
        id: 1,
        title: 'Countries',
        link: '#countries'
    }, {
        id: 2,
        title: 'Genres',
        link: '#genres'
    },
    {
        id: 3,
        title: 'Awards',
        link: '#awards'
    }, {
        id: 4,
        title: 'Release Year',
        link: '#release-year'
    }, {
        id: 5,
        title: 'Actors',
        link: '#actors'
    }, {
        id: 6,
        title: 'Tropes',
        link: '#tropes'
    }
    ]
},
{
    id: 3,
    mainMenuLink: {
        title: 'Conclusion',
        link: '#conclusion'
    },
    secondaryMenuLinks: [
        {
            id: 1,
            title: "What's next?",
            link: '#next'
        }]
}, {
    id: 4,
    mainMenuLink: {
        title: 'The Kitchen',
        link: '#playground'
    },
    secondaryMenuLinks: []
}]

function setIsMobileMenuOpen(value) {
    isMobileMenuOpen.value = value
}

onMounted(() => {
    window.addEventListener('resize', handleWindowSizeChange)
    handleWindowSizeChange()
})
onUnmounted(() => {
    window.removeEventListener('resize', handleWindowSizeChange)
})
const handleWindowSizeChange = () => {
    if (window.innerWidth >= 768) { // Tailwind’s md breakpoint
        setIsMobileMenuOpen(false)
    }
}
</script>
  