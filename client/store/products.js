export const state = () => ({

});

export const mutations = {

};

export const actions = {
  async createProduct (commit, payload) {
    const form = new FormData();
    for (const field in payload) {
      form.append(field, payload[field]);
    }
    return await this.$axios
      .post('/product/upload', form)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async updateProductDetails (commit, payload) {
    const { ID, ...data } = payload;
    const form = new FormData();
    for (const field in data) {
      form.append(field, data[field]);
    }
    return await this.$axios
      .put(`/product/${payload.ID}/update`, form)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async getFarmersProducts (commit, payload) {
    return await this.$axios
      .get('/user/products', {
        params: {
          ...payload
        }
      })
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async productsByCategory (commit, payload) {
    return await this.$axios
      .get('/products/category', {
        params: {
          ...payload
        }
      })
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async deleteProductById (commit, ID) {
    return await this.$axios
      .delete(`/product/${ID}/delete`)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async getProductById (commit, ID) {
    return await this.$axios
      .get(`/product/${ID}`)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async getProductOwerInfo (commit, ID) {
    return await this.$axios
      .get(`/product/${ID}/farmer`)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async getUserOrderlist (commit) {
    return await this.$axios
      .get('/user/orders')
      .then(res => {
        return res.data;
      })
      .catch(err => {
        return err;
      });
  },

  async createOrder (commit, payload) {
    return await this.$axios
      .post('/user/product/order', payload)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async confirmOrder (commit, payload) {
    return await this.$axios
      .post('/user/product/order/confirmation', payload)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  }
};

export const getters = {

};
