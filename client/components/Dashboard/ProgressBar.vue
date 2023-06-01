<template>
  <b-progress
  :value="value"
  :variant="variant"
  :striped="striped"
  class="mb-2"
  height="5px">
  </b-progress>
</template>

<script>
export default {
  name: 'ProgressBar',
  props: {
    value: {
      type: Number,
      defualt: 50,
      required: true
    }
  },
  data () {
    return {
      striped: true
    }
  },
  computed: {
    variant () {
      return this.value > 60 ? 'success' : 'info';
    }
  }
}
</script>

<style>

</style>