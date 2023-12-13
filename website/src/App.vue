<script setup>
import Navbar from './Navbar.vue'
import { ref } from 'vue'

const activeLamp = ref(true)

function toggleLamp() {
  activeLamp.value = !activeLamp.value
}

</script>

<template>
  <Navbar />

  <!-- Hero -->
  <div
    class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
    <h1 class="text-3xl lg:text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">Why the New
      York Times
      doesn't like
      Marvel movies</h1>
    <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain movie
      taste differences between users and critics</h3>
    <div class="flex flex-col items-center mt-auto px-5 py-3">
      <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] mt-3">A project by</span>
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
  <main class="grid grid-cols-5 w-full items-center overflow-hidden">
    <div class="cols-1 pl-8">
      <div class="lamp-container">
        <img :src="activeLamp ? '/lamp_right.png' : '/lamp_face.png'" alt="lamp face" class="lamp cursor-pointer"
          @click="toggleLamp" />
        <svg v-show="activeLamp" class="light-aura" width="1000" height="600" viewBox="0 0 500 300" preserveAspectRatio="xMidYMin slice">
          <polygon points="350,100 800,100 204,6 197,16" fill="yellow" />
          <!-- Adjust the points to shape the cone as needed -->
        </svg>
      </div>
    </div>
    <div class="flex col-span-3 flex-col p-8 w-full max-w-screen-lg">
      <section id="introduction" class="section">
        <h2 class="text-3xl font-bold mt-5">Introduction</h2>
        <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
          consequat
          aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>


        <section id="users" class="section">
          <h3 class="text-2xl font-bold mt-8">Users</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="critics" class="section">
          <h3 class="text-2xl font-bold mt-8">Critics</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="different-tastes" class="section">
          <h3 class="text-2xl font-bold mt-8">Different tastes</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>
      </section>

      <section id="exploration" class="section">
        <h2 class="text-3xl font-bold mt-8">Exploration</h2>

        <section id="genres" class="section">
          <h3 class="text-2xl font-bold mt-8">Genres</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="awards" class="section">
          <h3 class="text-2xl font-bold mt-8">Awards</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="countries" class="section">
          <h3 class="text-2xl font-bold mt-8">Countries</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="release-year" class="section">
          <h3 class="text-2xl font-bold mt-8">Release Year</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="runtime" class="section">
          <h3 class="text-2xl font-bold mt-8">Runtime</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="actors" class="section">
          <h3 class="text-2xl font-bold mt-8">Actors</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="plot" class="section">
          <h3 class="text-2xl font-bold mt-8">Plot</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>
      </section>

      <section id="conclusion" class="section">
        <h2 class="text-2xl font-bold mt-8">Conclusion</h2>
        <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
          consequat
          aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
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
}</style>
