<template>
    <div>
        <div class="header-wrapper">
            <div class="header-back" @click="handleBackClick">
                <img class="header-back-img" src="../../assets/img/header-back.png" alt="">
            </div>
        </div>
    </div>
</template>

<script>
    import {
        mapState,
        mapGetters,
        mapActions
    } from 'vuex'
    export default {
        name: 'SettingHeader',
        data() {
            return {
                sendDatasOff: {
                    'JA': {
                        'JA': [0, 0]
                    },
                    'JB': {
                        'JB': [0, 0]
                    },
                    'SS': {
                        'SS': ['off', 0, 0.5]
                    },
                    'SM': {
                        'SM': ['off', 0, 0.5]
                    },
                    'SL': {
                        'SL': ['off', 0, 0.5]
                    },
                    'TT': {
                        'TT': ['off', 'you']
                    },
                    'US': {
                        'US': 'off'
                    },
                    'GS': {
                        'GS': "off"
                    },
                    'OA': {
                        'OA': 'off'
                    },
                    'TL': {
                        "TL": ['off', 400]
                    },
                    'CD': {
                        'CD': ['off', 110]
                    },
                    'CA': {
                        'CA': 'off'
                    },
                    'HT': {
                        'HT': 'off'
                    },
                    'HF': {
                        'HF': 'off'
                    },
                    'CT': {
                        'CT': 'off'
                    },
                    'CF': {
                        'CF': 'off'
                    },
                    'MS': {
                        'MS': ['off', 0, 0]
                    },
                    'DO': {
                        'DO': 0
                    },
                    'PO': {
                        'PO': 0
                    },
                    'TO': {
                        'TO': 0
                    },
                    'CC': {
                        'CC': 'blue'
                    },
                },
            }
        },
        methods: {
            ...mapActions(['send']),
            handleBackClick() {
                // this.send(this.sendDatasOff);
                this.$router.push('/controll')
            }
        }
    }
</script>

<style scoped>
    .header-wrapper {
        height: 1rem;
        display: flex;
        background: #10243b;
    }

    .header-back {
        float: left;
        padding: 0 .25rem;
        line-height: 1rem;
    }

    .header-back-img {
        width: 80%;
    }
</style>