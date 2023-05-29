<template>
    <div>
    <TheHeader></TheHeader>
    <Nuxt />
    <TheFooter></TheFooter>
  </div>
</template>

<script>
import cssVars from '~/utils/cssVariables.json';

export default {
  name: 'DefaultLayout'

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