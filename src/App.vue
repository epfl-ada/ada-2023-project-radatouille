<script setup>
import Navbar from './Navbar.vue'
</script>

<template>
  <Navbar />

  <!-- Hero -->
  <div
    class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
    <h1 class="text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">Why the New York Times
      doesn't like
      Marvel movies</h1>
    <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain movie
      taste differences between users and critics</h3>
    <div class="flex flex-col items-center mt-auto px-5 py-3">
      <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">A project by</span>
      <div class="flex flex-wrap gap-1 items-center justify-center">
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
  <main class="flex flex-col w-full items-center">
    <div class="flex flex-col p-8 w-full max-w-screen-lg">
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
</style>
