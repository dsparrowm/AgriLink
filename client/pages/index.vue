<template>
  <div class="site-container">
    <h1 style="background-color: var(--clr-primary-dkr);">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, blanditiis. Aspernatur veritatis deserunt, tempora voluptate deleniti minima. Nam inventore ducimus quia sint dolores, ad laborum perferendis iure reiciendis ipsam laboriosam?</h1>
    Landing Page goes here...... 
    <h2>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis dicta aliquid distinctio iste maxime vel, voluptates, sit illo nemo hic nam dolorem perspiciatis sint nostrum! Quis corrupti maxime in facilis!</h2>
    <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, quos iure. Nam ad quisquam dicta optio, laudantium quod repellendus iusto error aperiam maxime consequuntur, voluptatum quasi voluptas ut fuga laboriosam?</h3>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';
export default {
  name: 'IndexPage',
  layout: 'main',

  head:{
    title: 'AgriLink | Home'
  },

  methods: {
    ...mapActions({
      status: 'status',
    }),
  },
  mounted () {
    this.status();
  }
}
</script>

