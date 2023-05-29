<template>
  <div class="wrapper">
    <div class="backdrop">
      <form class="form" @submit.prevent="submitForm">
        <slot></slot>
        <div class="form__group form__actions">
          <button class="btn form__update" type="submit">UPDATE</button>
          <button 
          class="btn form__cancel" 
          type="reset"
          @click="closeForm">CANCEL</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserInfoUpdateForm',
  methods: {
    submitForm () {
      this.$emit('update');
    },
    closeForm () {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>
.wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
}
.backdrop {
  height: 100%;
  width: 100%;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
}
.form {
  border-radius: 5px;
  background-color: var(--clr-ntrl-min);
  width: 100%;
  padding: 1rem;
}

@media (min-width: 48.0625em) {
  .form {
    max-width: 500px;
    margin: 0 auto;
  }
}
.form__actions {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.form__update {
  color: var(--clr-ntrl-min);
  background-color: var(--clr-primary);
}
.form__cancel {
  color: var(--clr-ntrl-min);
  background-color: var(--clr-base-lt);
}

</style>