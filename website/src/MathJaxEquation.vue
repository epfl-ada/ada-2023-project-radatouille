<template>
    <div ref="mathContainer" v-html="equation"></div>
  </template>
  
  <script>
  import { onMounted, ref, watch, nextTick } from 'vue';
  import 'mathjax/es5/tex-mml-chtml';
  
  export default {
    name: 'MathJaxEquation',
    props: {
      equation: String,
    },
    setup(props) {
      const mathContainer = ref(null);
  
      const renderMath = async () => {
        await nextTick();
        window.MathJax.typesetPromise([mathContainer.value]);
      };
  
      onMounted(renderMath);
      watch(() => props.equation, renderMath);
  
      return { mathContainer };
    },
  };
  </script>
  