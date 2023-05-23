<template>
    <div>
    <TheHeader />
    <Nuxt />
    <TheFooter />
  </div>
</template>

<script>
import cssVars from '~/utils/cssVariables.json';

export default {

    // mounted: function(){
    //     console.log(cssVars);
    //     Object.keys(cssVars).forEach(key => {
    //         if (cssVars[key]) {
    //             document.documentElement.style.setProperty(key, cssVars[key]);
    //         }
    //     })
    // }

}
</script>

<style>

</style>