import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    details: "",
    allProducts: [],
    cart: [],
  },
  getters: {
    productDetails: (state) => (index) => { 
        return state.allProducts[index];
    },
    allProducts(state) {
      return state.products
    },
    getCart(state){
      return state.cart
    }
  },
  mutations: {
    setProducts(state, products) {
      state.allProducts = products
    },
    addCart(state, product) {
      state.cart.push(product)
    },
    clearCart(state){
      state.cart = []
    },
  },
  actions: {
    
  },
  modules: {
  }
})
