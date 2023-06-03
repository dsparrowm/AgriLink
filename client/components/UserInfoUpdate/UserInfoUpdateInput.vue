<template>
      <div class="form__group">
        <input
        class="form__input"
        :type="inputType"
        :id="inputId"
        :name="inputName"
        v-model="inputData"
        :placeholder="'Enter new ' + displayMsg"
        required
        >
        <template
        v-if="isNameField">
        <p class="text-info">
          Note: The full name must consist of two words. If more than two words are provided, only the first and second words will be saved.
        </p>
        </template>
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
  computed: {
    isNameField () {
      return this.inputName === 'name';
    },
    displayMsg () {
      return this.isNameField ? 'full name' : this.inputName;
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