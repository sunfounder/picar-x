<template>
    <div>
        <div class="connection-wrapper">
            <!-- <p class="connection-title">Please enter the IP address:</p> -->
            <!-- <div class="connection-input-wrapper">
                <input v-model="first" type="number" class="connection-input" />
                <span>·</span>
                <input v-model="second" type="number" class="connection-input" />
                <span>·</span>
                <input v-model="third" type="number" class="connection-input" />
                <span>·</span>
                <input v-model="forth" type="number" class="connection-input" />
            </div> -->
            <div class="connection-btn-wrapper">
                <div class="connection-btn" @click="handleConnectionCLick">
                    <img class='connection-btn-img' src="../../assets/img/home_btn.png" alt="">
                </div>
            </div>
        </div>
        <Alert v-model="isConnect" :data="alert" closeOnClickModal @ok="ok" />
    </div>
</template>

<script>
    import {
        mapState,
        mapMutations,
        mapActions
    } from 'vuex'
    export default {
        name: 'HomeConnection',
        data() {
            return {
                first: 0,
                second: 0,
                third: 0,
                forth: 0,
                ...mapState(['socket', 'messageSocket']),
                isConnect: false,
                alert: {
                    title: 'success',
                    content: 'connect websocket success',
                    alertBtn: 'OK',
                },
                isFail:false
            }
        },
        computed: {
            IP() {
                return `ws://${location.hostname}:8765`
            },
            hostIp() {
                return `ws://${location.hostname}:8766`
            }
        },
        methods: {
            ...mapActions(['connectionSocket', 'connectionMessageSocket', 'open', 'wsError', 'getMessage', 'close']),
            ...mapMutations(['setSocket']),
            handleConnectionCLick() {
                this.connectionSocket(this.IP);
                this.connectionMessageSocket(this.hostIp);
                this.open(this.connectionSuccess);
                this.wsError(this.fail);
                this.getMessage();
                this.close(this.socketClose);
                this.$router.push("/controll")
            },
            connectionSuccess() {
                this.alert = {
                    title: 'success',
                    content: 'connect websocket success',
                    alertBtn: 'OK',
                },
                this.isConnect = false
                this.isFail = false
            },
            fail() {
                this.alert =  {
                    title: 'fail',
                    content: 'connect websocket fail',
                    alertBtn: '取消',
                }
                this.isConnect = true
                this.isFail = true
            },
            reConnect () {
                this.connectionSocket(this.IP);
                this.connectionMessageSocket(this.hostIp);
            },
            enterControll () {
                this.$router.push('/controll')
            },
            socketClose () {
                this.alert =  {
                    title: 'fail',
                    content: 'websocket is close, please connect',
                    alertBtn: 'OK',
                }
                this.isConnect = true
            },
            ok() {
                this.isConnect = false
                if (!this.isFail) {
                    this.enterControll();
                }
                
            }
        }
    }
</script>

<style scoped>
    .connection-wrapper {
        position: absolute;
        top: 2.6rem;
        right: 1.2rem;
        overflow: hidden;
    }

    .connection-title {
        line-height: .76rem;
        font-size: .32rem;
    }

    .connection-input-wrapper {
        display: flex;
    }

    .connection-input-wrapper span {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 .1rem;
        font-size: 0.6rem;
    }

    .connection-input {
        width: 1.54rem;
        height: .7rem;
        border-radius: 0.06rem;
        border: 1px solid #cccccc;
        text-align: center;
    }

    .connection-btn-wrapper {
        text-align: center;
        line-height: .8rem;
        margin-top: .3rem;
    }

    .connection-btn {
        height: 0;
        padding-bottom: 25.81%;
        overflow: hidden;
    }

    .connection-btn-img {
        width: 60%;
    }
</style>