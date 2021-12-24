import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    products: []
  },
  getters: {
    productDetails: (state) => (index) => { 
        return state.products[index];
    },
    allProducts(state) {
      return state.products
    }
  },
  mutations: {
    setProducts(state, products) {
      state.products = products
    }
  },
  actions: {
    init(context) {
          fetch("http://localhost:5000/get_dashboard")
          .then((response) => {
            // console.log(response);
            return response.json();
          })
          .then((data) => {
            console.log(data);
            context.commit('setProducts', data.data)
            // console.log(data);
          });
      },
  },
  modules: {
  }
})
