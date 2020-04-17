import Vue from 'vue'
import Vuex from 'vuex'
import state from './state'
import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters: {
        msgObj(state) {
            return JSON.parse(state.msg)
        },
        color_ (state) {
            return state.color
        },
        line_ (state) {
            return state.line
        },
        cliff_ (state) {
            return state.cliff
        },
        isClose_ (state) {
            return state.isClose
        }
    },
    modules: {}
})