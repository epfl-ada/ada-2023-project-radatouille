<template>
    <nav class="h-14 flex bg-dark text-light items-center justify-end sticky top-0 left-0 w-full z-10">
        <button class="cursor-pointer w-14 h-14 flex items-center justify-center " title="Open menu"
            @click="() => setIsMobileMenuOpen(true)">
            <span class="hover:bg-white/90 hover:text-dark rounded-full p-2">
                <Bars3Icon class="w-6 h-6 " />
            </span>
        </button>
    </nav>

    <!-- Mobile menu -->
    <TransitionRoot appear :show="isMobileMenuOpen" as="template">
        <Dialog as="div" @close="setIsMobileMenuOpen">
            <TransitionChild as="template" enter="duration-200 ease-out" enter-from="opacity-0" enter-to="opacity-100"
                leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-black/50 z-10" />
            </TransitionChild>

            <div class="fixed inset-0 overflow-y-auto overflow-x-hidden z-20">
                <TransitionChild as="template" enter="duration-200 ease-out" enter-from="opacity-0 translate-x-full"
                    enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100"
                    leave-to="opacity-0 translate-x-full">
                    <DialogPanel class="h-full ml-16 lg:w-1/3 lg:ml-auto">
                        <div class="bg-dark text-light h-full w-full overflow-y-auto p-8">
                            <button class="bg-slate-500 rounded-full p-3 text-white fixed top-8 right-8 hover:bg-slate-600"
                                title="Close menu" @click="() => setIsMobileMenuOpen(false)">
                                <XMarkIcon class="w-6 h-6" />
                            </button>

                            <div v-for="section in sections" :key="section.id" class="mt-4">
                                <h3 class="text-3xl font-medium mt-4">
                                    <a class="flex gap-3 items-center py-2 hover:text-slate-400"
                                        :href="section.mainMenuLink?.link" @click="() => setIsMobileMenuOpen(false)">
                                        <span>{{ section.mainMenuLink?.title }}</span>
                                        <ChevronRightIcon class="w-6 h-6" />
                                    </a>
                                </h3>
                                <a v-for="link in section.secondaryMenuLinks" :key="link.id"
                                    class="text-xl block py-2 hover:text-slate-400" :href="link.link"
                                    @click="() => setIsMobileMenuOpen(false)">
                                    {{ link.title }}
                                </a>
                            </div>
                        </div>
                    </DialogPanel>
                </TransitionChild>
            </div>
        </Dialog>
    </TransitionRoot>
</template>
  
<script setup>
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel
} from '@headlessui/vue'

import { Bars3Icon, ChevronRightIcon, XMarkIcon } from '@heroicons/vue/24/solid'
import { ref, onMounted, onUnmounted } from 'vue'

const isMobileMenuOpen = ref(false)

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
    secondaryMenuLinks: []
}, {
    id: 4,
    mainMenuLink: {
        title: 'Playground',
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
  