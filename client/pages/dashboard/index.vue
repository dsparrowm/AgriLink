<template>
  <div class="page-wrapper">
    <h1>
      Sales Analytics
    </h1>
    <!-- Farmer Sales and Product Perfromance Cards -->
    <div class="performance">
      <div class="performance__row">
        <template
        v-if="balances">
          <div class="monthly-card mb-3">
            <span class="text-muted">
              Total Balance: 
            </span>
            <span class="font-weight-bold text-success">
              {{ formatNumberAsDecimal(balances.balance) }}
            </span>
          </div>
      </template>
        <!-- Account balances Section -->
        <!-- <div
        class="performance__account">
          <div class="left l-flex">
            <div class="total__bal flex-box monthly-card">
              <div class="icon-wrapper bg-secondary">
                <span class="icon-md">
                  <font-awesome-icon :icon="['fas', 'dollar-sign']" />
                </span>
              </div>
              <div>
                <h6>Total Balances</h6>
                <span class="font-weight-bold">
                  &#8358; {{ formatNumberAsDecimal() }}
                </span>
              </div>
            </div>
            <div class="available__bal flex-box monthly-card">
              <div class="icon-wrapper bg-success">
                <span class="icon-md">
                  <font-awesome-icon :icon="['fas', 'dollar-sign']" />
                </span>
              </div>
              <div>
                <h6>Available Balance</h6>
                <span class="font-weight-bold">
                  &#8358; {{ formatNumberAsDecimal() }}
                </span>
              </div>
            </div>
          </div>
          <div class="pending__bal flex-box monthly-card right">
            <div class="icon-wrapper bg-primary">
              <span class="icon-md">
                <font-awesome-icon :icon="['fas', 'dollar-sign']" />
              </span>
            </div>
            <div>
              <h6>Pending Balance</h6>
              <span class="font-weight-bold">
                &#8358; {{ formatNumberAsDecimal() }}
              </span>
            </div>
          </div>
        </div> -->
        <!-- Sales Summary Section -->
        <template>
          <div class="performance__totals">
            <div class="left l-flex">
              <div class="total__sales monthly-card flex-box">
                <div class="icon-wrapper bg-warning">
                  <span class="icon-md">
                    <font-awesome-icon :icon="['fas', 'dollar-sign']" />
                  </span>
                </div>
                <div>
                  <h6>Total Sales</h6>
                  <span class="font-weight-bold">
                    &#8358; {{ formatNumberAsDecimal(salesSummary.total_sales) }}
                  </span>
                </div>
              </div>
  
              <div class="total__orders monthly-card flex-box">
                <div class="icon-wrapper bg-success">
                  <span class="icon-md">
                    <font-awesome-icon icon="shopping-cart"/>
                  </span>
                </div>
                <div>
                  <h6>Total Orders</h6>
                  <span class="font-weight-bold">
                    {{ salesSummary.total_orders || 0 }}
                  </span>
                </div>
              </div>
            </div>
  
            <div class="total__products monthly-card right flex-box">
              <div class="icon-wrapper bg-primary">
                <span class="icon-md">
                  <font-awesome-icon icon="shopping-basket"/>
                </span>
              </div>
              <div>
                <h6>Total Products</h6>
                <span class="font-weight-bold">
                  {{ salesSummary.total_products || 0 }}
                </span>
              </div>
            </div>
          </div>
        </template>
      </div>

      <!-- Charts Section -->
      <div class="performance__row charts">
        <div class="total_s-chart left">
          <h4>Monthly Revenue</h4>
          <client-only
            v-if="totalSalesData"
            placeholder="Loading..."
          >
            <LineChart
              :chart-options="barChartOptions"
              :chart-data="totalSalesData"
              :height="250"
              chart-id="totalSales"
            />
          </client-only>
        </div>
        <div class="product_s-chart right">
          <h4>By Product</h4>
          <client-only
            v-if="byPoductsSalesData"
            placeholder="Loading..."
          >
            <LineChart
              :chart-options="barChartOptions"
              :chart-data="byPoductsSalesData"
              :height="250"
              chart-id="totalSales"
            />
          </client-only>
        </div>
        <!-- <monthly-revenue></monthly-revenue>
        <monthly-unit-sold></monthly-unit-sold>
        <monthly-orders></monthly-orders>
        <monthly-summary></monthly-summary> -->
      </div>
    </div>
    <template
    v-if="orderList.length">
    <div
    class="latest-orders mt-4">
      <h4>Latest orders</h4>
      <div
      class="latest-orders__table">
        <order-list-table
          :fields="fields"
          :table-body="orderList">
        </order-list-table>
      </div>
    </div>
    </template>
  </div>
</template>

<script>
import {
  mapMutations,
  mapActions,
  mapGetters
} from 'vuex';
import OrderListTable from '../../components/OrderListTable.vue';
export default {
  components: { OrderListTable },
  name: 'DashboardIndexPage',
  layout: 'dashboard',
  middleware: ['auth'],

  head: {
    title: 'AgriLink | Dashboard'
  },

  data () {
    return {
      balances: {},
      salesSummary: {},
      orders: [],
      fields: [
        {key: 'order_id', label: 'Order #'},
        'date',
        'amount',
        'product_name',
        'buyer_name',
        'status',
      ],
      barChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        pointStyle: 'star',
        barThickness: 3,
        hoverOffset: 4,
        legend: {
          display: true,
          title: 'Pie Chart Samples'
        },
        title: {
          display: true,
          text: 'Customer analytics data',
          fontSize: 24,
          fontColor: '#6b7280'
        },
        tooltips: {
          backgroundColor: '#17BF62'
        },
        scales: {
          y: {
            ticks: {
              beginAtZero: true,
              callback: function(value, index, ticks) {
                return '$' + value + ' K ';
              }              
            },
            grid: {
              display: true,
            }
          },
          x: {
            grid: {
              // display: false
            }
          }
        }
      },
      totalSalesData: null,
      byPoductsSalesData: null
    }
  },

  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),

    orderList () {
      return this.orders;
    }
  },

  methods: {
    ...mapActions({
      userOrderList: 'products/getUserOrderlist',
      getSalesSummary: 'getSalesSummary',
      getUserBalances: 'getUserBalances',
    }),
      
    async fetchSalesSummary () {
      try {
        const res = await this.getSalesSummary();
        if (res.status === 200) {
          this.salesSummary = res.data;
        }
      } catch (error) {
        console.error(error);
      }
    },

    async fetchUserBalances () {
      try {
        const res = await this.getUserBalances(this.userObj.id);
        if (res.status === 200) {
          this.balances = res.data;
        }
      } catch (error) {
        console.error(error);
      }
    },

    async getOrderList () {
      try {
        const res = await this.userOrderList();
        this.orders = res.Transactions;
        if (this.orders.length) {
          this.orders.map(item => {
            item.date = this.$moment(item.createad_at)
            .format("DD.MM.YYYY");
          });
        }
      } catch (error) {
        console.error(error);
      }
    },

    formatNumberAsDecimal (val = 0) {
      return parseFloat(val)
        .toFixed(2)
        .replace(/\d(?=(\d{3})+\.)/g, '$&,');
    }
  },

  mounted () {
    this.fetchUserBalances();
    this.fetchSalesSummary();
    this.getOrderList();
    this.totalSalesData = {
      // labels: [...(this.sales && this.sales.map((item) => item.name))],
      // datasets: [
      //   {
      //     label: 'Visualization',
      //     data: [...(this.sales && this.sales.map((item) => item.summary))],
      //     backgroundColor: 'rgba(101, 110, 10, 0.75)',
      //     borderColor: 'rgba(140, 155, 0, 1)',
      //     borderWidth: 1
      //   }
      // ]
      type: 'Line',
      labels: ['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'],
      datasets: [
        {
          label: 'Total Monthy Sales',
          data: [0, 300, 500, 40, 200, 100, 700],
          backgroundColor: 'rgba(101, 110, 10, 0.75)',
          borderColor: 'rgba(140, 155, 0, 1)',
          borderWidth: 2,
          lineTension: 0.1,
        }
      ],
    }
    this.byPoductsSalesData = {
      type: 'Line',
      labels: ['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'],
      datasets: [
        {
          label: 'product name',
          data: [0, 500, 100, 40, 200, 300],
          backgroundColor: 'rgba(242, 204, 685)',
          borderColor: 'rgba(242, 204, 685)',
          borderWidth: 2,
          lineTension: 0.1,
        },
        {
          label: 'product name',
          data: [0, 200, 400, 40, 100, 50],
          backgroundColor: 'rgba(50, 168, 162)',
          borderColor: 'rgba(50, 168, 162)',
          borderWidth: 2,
          lineTension: 0.1,
        },
        {
          label: 'product name',
          data: [100, 0, 500, 40, 200, 600],
          backgroundColor: 'rgba(9, 61, 230)',
          borderColor: 'rgba(9, 61, 230)',
          borderWidth: 2,
          lineTension: 0.1,
        }
      ],
    }
  }
}
</script>

<style scoped>
.performance {
  margin-top: 2rem;
}

.latest-orders,
.monthly-card {
  background-color: var(--clr-ntrl-min);
  border-radius: 3px;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
  padding: 0.5rem;
}


.monthly-card  h6 {
  margin-bottom: 0;
  font-size: var(--fs-milli);
  font-weight: 500;
  color: var(--clr-base-lt);
}

.total__bal,
.available__bal,
.total__sales,
.total__orders {
  flex: 1;
}

.flex-box {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  margin-bottom: 1.5rem;
}

.performance__account,
.performance__totals,
.l-flex,
.charts {
  display: flex;
  gap: 1.5rem;
}

.left {
  width: 65%;
}

.right {
  width: 35%;
}

@media (max-width: 68.0625em) {
  .total__bal,
  .available__bal,
  .total__orders,
  .total__sales {
    margin-bottom: 0;
  }

  .performance__account,
  .performance__totals,
  .l-flex,
  .charts {
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 0;
  }

  .right,
  .left {
    width: 100%;
  }
  
  .latest-orders {
    display: none;
  }
}

.total_s-chart,
.product_s-chart {
  background-color: var(--clr-ntrl-min);
  padding: 1rem;
  border-radius: 3px;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

.icon-wrapper {
  border-radius: 50%;
  background-color: #E6E6E6;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  width: 50px;
  padding: 0.5rem;
}

.icon-md {
  font-size: 1.5rem;
  color: var(--clr-ntrl-min);
}
</style>