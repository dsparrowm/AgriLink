<template>
      <div class="form__group">
        <input
        class="form__input"
        :type="inputType"
        :id="inputId"
        :name="inputName"
        v-model="inputData"
        :placeholder="'update ' + inputName"
        required
        >
      </div>
</template>

<script>
export default {
  name: 'UserInfoUpdateInput',
  props: {
    inputType: {
      type: String,
      default: 'text',
      required: false
    },
    inputName: {
      type: String,
      default: 'name',
      required: true
    },
    inputId: {
      type: String,
      default: 'user',
      required: true
    }
  },
  data () {
    return {
      inputData: ''
    }
  },
  watch: {
    inputData (val) {
      this.$emit('inputedData', val);
    }
  }
}
</script>

<style scoped>
.form__group {
  margin-bottom: 0.5rem;
}
.form__input {
  border: 1px solid var(--clr-base-lt);
  border-radius: 5px;
  outline: none;
  padding: 10px;
  width: 100%;
}
.form__input:focus,
.form__input:active {
  outline: 1px solid var(--clr-primary);
}
</style>