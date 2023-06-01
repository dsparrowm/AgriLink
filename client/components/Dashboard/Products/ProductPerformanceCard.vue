<template>
  <div class="performance">
    <h5 class="mb-3">By product</h5>
    <div v-for="(item, i) in performance" :key="i"
    class="performance__item">
      <h6>
        <span class="performance__name">
          {{ item.productName }}
        </span>
        <span class="performance__name">
          <template v-if="isAmount">
            {{ `$${item.value}` }}
          </template>
          <template v-else-if="isUnit">
            {{ `${item.value} k` }}
          </template>
          <template v-else>
            {{ item.value }}
          </template>
        </span>
      </h6>
      <progress-bar
      :value="item.progress">
      </progress-bar>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import ProgressBar from '../ProgressBar.vue';
export default {
  name: 'ProductPerformanceCard',
  props: {
    performance: {
      type: Array,
      required: true,
      default: []
    },
    ticks: {
      type: String,
      required: false,
      default: ''
    }
  },
  components: {
    ProgressBar
  },
  computed: {
    isAmount () {
      return this.ticks === 'amount';
    },

    isUnit () {
      return this.ticks === 'unit';
    }
  }
}
</script>

<style scoped>
.performance__item h6 {
  display: flex;
  font-size: var(--fs-milli);
  justify-content: space-between;
  /* margin-bottom: 0; */
}

</style>