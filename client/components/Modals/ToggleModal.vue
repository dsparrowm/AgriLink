<template>
  <div class="modal">
    <h2 class="modal__heading">
      <span class="drop_left">
          {{ title }}
      </span>
      <button
      @click="toggleModal"
      class="modal__toggle">
        <span class="icon-mini ml-2 drop_right">
          <template v-if="showModal">
              <font-awesome-icon icon="angle-up"/>
          </template>
          <template v-else>
              <font-awesome-icon icon="angle-down"/>
          </template>
        </span>
      </button>
    </h2>
    <div class="modal__content modal__content--show-hide">
      <slot></slot>
    </div> 
  </div>
</template>

<script>
export default {
  name: 'ToggleModal',
  props: {
    title: {
      type: String,
      default: '',
      required: true
    }
  },
  data () {
    return {
      showModal: false
    }
  },
  methods: {
    toggleModal () {
      this.showModal = !this.showModal;
    }
  }
}
</script>

<style scoped>
</style>