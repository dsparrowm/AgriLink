<template>
  <div class="my-orders">
    <!-- Will only render on medium & large screens -->
    <div class="my-orders__table">
      <b-table
      striped
      hover
      :fields="fields"
      :items="tableBody">
      
      <template
       #cell(amount)="row">
        <span>
          &#8358;{{ row.item.amount }}
        </span>
      </template>
      <template
       #cell(status)="row">
        <span
        class="rounded text-white p-1"
        :class="{
        'bg-success': row.item.status === 'completed',
        'bg-danger': row.item.status !== 'completed'}
        ">
          {{ row.item.status }}
        </span>
      </template>
  
        <template #cell(action)="row">
            <template
            v-if="row.item.status !== 'completed'">
              <b-button
              size="sm"
              class="btn confirm-btn"
              :disabled="row.item.status === 'completed'"
              @click="updateOrderStatus(row.item)">
                Confirm
              </b-button>
            </template>
        </template>
      </b-table>
    </div>
    <!-- Will only render on small screens -->
    <div class="my-orders__items p-2">
      <article
      v-for="(item, i) in tableBody" :key="i">
      <!-- {{ item }} -->
        <p class="m-0">
          <span class="font-weight-bold mr-2">Order #:</span> {{ item.order_id }}
        </p>
        <p class="m-0">
          <span class="font-weight-bold mr-2">Date:</span> {{ item.date }}
        </p>
        <!-- <p class="m-0">
          <span class="font-weight-bold mr-2">Ship To:</span> {{ item.ship_to }}
        </p> -->
        <p class="m-0">
          <span class="font-weight-bold mr-2">Product Name:</span> {{ item.product_name }}
        </p>
        <p class="m-0">
          <span class="font-weight-bold mr-2">Amount:</span> &#8358;{{ item.amount }}
        </p>
        <p class="m-0">
          <span class="font-weight-bold mr-2">Status:</span> {{ item.status }}
        </p>
        <p 
        v-if="item.status !== 'completed'"
        class="m-0">
          <span class="font-weight-bold mr-2">Action:</span>
          <b-button
            size="sm"
            class="btn confirm-btn"
            :disabled="item.status === 'completed'"
            @click="updateOrderStatus(item)">
              Confirm
          </b-button>
        </p>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderListTable',
  props: {
    tableBody : {
      type: Array,
      required: true,
      default: []
    },

    fields : {
      type: Array,
      required: true
    }
  },

  methods: {
    updateOrderStatus (order) {
      this.$emit('confirm-order', order);
    }
  }
}
</script>

<style scoped>
.my-orders__table {
  display: none;
}
.my-orders__items > * + * {
  margin-top: 2rem;
}

/* Applies to medium to large screen sizes */
@media (min-width: 48.0625em) {
  .my-orders__table {
    display: block;
  }

  .my-orders__items {
    display: none;
  }
}

.confirm-btn {
  background-color: var(--clr-primary-dkr);
  color: var(--clr-ntrl-min);
  border: none;
}
</style>