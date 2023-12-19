<template>
    <div v-if="isOpen" class="fixed inset-0 w-full bg-black/50 z-10" @click="handleClose">
        <!-- Overlay -->
    </div>

    <div v-if="isOpen" class="fixed z-20 w-full" :style="{ top: position.top + 'px', left: position.left + 'px' }" @click.stop ref="dialog">
        <!-- Dialog content -->
        <slot></slot>
    </div>
</template>
  
<script setup>
import { ref, watch, onMounted } from 'vue';
import { useFloating, offset, flip } from '@floating-ui/vue';

const props = defineProps({
    isOpen: Boolean,
    anchorEl: Object
});

const emit = defineEmits(['close']);

function handleClose() {
  emit('close'); // Emit the 'close' event to the parent component
}

const placement = ref('bottom-start')
const middleware = ref([offset(10), flip()])

useFloating(placement, middleware, { enabled: props.isOpen });

const dialog = ref(null);
const position = ref({ top: 0, left: 0 });

watch(() => props.isOpen, (newVal) => {
  if (newVal && props.anchorEl) {
    const { top, left } = props.anchorEl.getBoundingClientRect();
    position.value = { top, left };
  }
});


</script>

  