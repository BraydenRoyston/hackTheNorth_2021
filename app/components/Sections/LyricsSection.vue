<template>
    <div class="lyrics">
        <BarsTop id="barsTop"/>
        <transition-group id="group" name="group">
            <div class="enterLyrics" key="1">
                <textarea 
                    name="lyrics" 
                    id="" 
                    cols="80" 
                    rows="20"
                    placeholder="Enter the lyrics of your favourite song here!!"
                    v-model="lyrics"
                >
                </textarea>
                <button class="submitLyrics" @click="fetchSomething">Calculate</button>
            </div>
            <div v-if="clicked" class="result" key="2">
                <ResultCard 
                    :overall="overall"
                    :rhyme="rhyme"
                    :semantic="semantic"
                    :repeat="repeat"
                />
            </div>
        </transition-group>
    </div>
</template>

<script>
import BarsTop from '../Layout/BarsTop.vue';
import ResultCard from '../Layout/ResultCard.vue'

export default {
    components: {
        BarsTop,
        ResultCard,
    },
    data() {
        return {
            clicked: false,
            lyrics: "",
            overall: 0,
            rhyme: 0,
            semantic: 0,
            repeat: 8,
            ip: "",
        }
    },
    methods: {
        async handleClick() {
            this.clicked = true;
            console.log(this.lyrics);

            // API call
            const response = await this.$axios.$get('localhost:5000');
            console.log(response);

            const epsilon_up = Math.floor(Math.random() * 2);
            const episilon_down = Math.floor(Math.random() * 2);
            this.rhyme = this.repeat + epsilon_up;
            this.semantic = this.repeat - episilon_down;
            this.overall = Math.floor((this.rhyme + this.semantic + this.repeat) / 3);
        }
    }
}
</script>

<style scoped>
.lyrics {
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;

    background: var(--black);
}

.enterLyrics {
    height: 50vh;
    /* width: 100%; */

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#group {
    height: 100%;
    width: 100%;

    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.group-enter-active, .group-leave-active {
  transition: all 1s;
}
.group-enter, .group-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}

textarea {
    font-family: var(--font-body);

    border-radius: 20px;
    padding: 10px;
    resize: none;
}

textarea:focus {
    border-radius: 20px !important;
    outline: none !important;
    border:1px solid var(--light-blue);
}

button {
    margin: 10px;
    padding: 10px 20px 10px 20px;
    
    border: 1px solid white;
    border-radius: 25px;
    background: transparent;


    font-family: var(--font-body);
    color: white;

    transition: all 1s ease;
    cursor: pointer;
}

button:hover {
    background: var(--blue);
}

#barsTop {
    position: absolute;
}
</style>