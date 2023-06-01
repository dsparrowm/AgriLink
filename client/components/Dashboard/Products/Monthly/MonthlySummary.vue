<template>
  <div class="monthly-summary">
    <div class="monthly-summary__item">
      <article class="monthly-summary__card monthly-card mgin-but">
        <h5>Pending Orders</h5>
        <div class="monthly-summary__card">
          <span>
            4
          </span>
          <span>
            $500
          </span>
        </div>
      </article>
      <article class="monthly-summary__card monthly-card mgin-but">
        <h5>Confirmed Orders</h5>
        <div>
          <span>
            5
          </span>
          <span>
            $600
          </span>
        </div>
      </article>
    </div>
    <div class="monthly-summary__item">
      <article class="monthly-summary__card monthly-card mgin-but">
        <h5>Returned Orders</h5>
        <div>
          <span>
            1
          </span>
          <span>
            $100
          </span>
        </div>
      </article>
      <article class="monthly-summary__card monthly-card mgin-but">
        <h5>Opp created this year</h5>
        <div>
          <span>
            20
            <span class="">
              <span class="icon-md">
                
              </span>
              14%
            </span>
            LY
          </span>
          <span>
            $5
            <span class="">
              <span class="icon-md">
                
              </span>
              14%
            </span>
            LY
          </span>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MonthlySummary',
}
</script>

<style scoped>
.mgin-but {
  margin-bottom: 1.5rem;
}

</style>