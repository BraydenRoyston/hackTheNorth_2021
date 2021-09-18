<template>
  <div class="rootWrapper">
    <NavBar />
    <LandingSection />
    <LyricsSection />
    <HowSection />
  </div>
</template>

<script>
import NavBar from '../components/UI/NavBar.vue';
import LandingSection from '../components/Sections/LandingSection.vue';
import LyricsSection from '../components/Sections/LyricsSection.vue'

export default {
  components: {
    NavBar,
    LandingSection,
    LyricsSection,
  }
}
</script>

<style>
/* Styles in this file are global. */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Quicksand:wght@300;400&display=swap');

/* https://coolors.co/00a6fb-0582ca-006494-003554-051923 */


:root {
  /* remove some defaults */
  overflow-x: hidden;
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  /* Typography styles */
  --font-header: 'Bebas Neue';
  --font-body: 'Quicksand';
  font-size: 8px;
  --fs-huge: clamp(3rem, calc(15vw + 3rem), 20rem);
  --fs-large: clamp(1.5rem, calc(3vw + 1rem), 5rem);
  --fs-medium: clamp(1.1rem, calc(2vw + 0.75rem), 3.5rem);
  --fs-small: clamp(1.5rem, calc(1.5vw + 0.5rem), 2.2rem);
  --fs-extra-small: clamp(0.75rem, calc(1vw + 0.5rem), 1.9rem);

  --black: #051923;
  --blue: #006494;
  --light-blue: #00A6FB;
}

body {
  margin: 0;
}

</style>
