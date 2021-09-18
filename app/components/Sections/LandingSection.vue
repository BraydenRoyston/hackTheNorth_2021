<template>
    <div class="landing">
        <div class="top"></div>
        <div class="textSpacing">
            <div class="space"></div>
            <div class="text">
                <h1>lyricalc</h1>
                <h3>The hip-hop taste of a robot.</h3>
            </div>
            <div class="space"></div>
        </div>
        <div class="bottom"></div>
        <BarsBottom id="barBottom"/>
    </div>
</template>

<script>
import BarsBottom from '../Layout/BarsBottom.vue';

export default {
    components: {
        BarsBottom,
    }
}
</script>

<style scoped>
.landing {
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: flex-start;

    background: var(--black);
}

.textSpacing {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.space {
    height: 100%;
    width: 10vw;
}

.text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
}

h1 {
    font-family: var(--font-header);
    font-size: var(--fs-huge);
    color: white;
    margin: 0;
}

h3 {
    font-family: var(--font-body);
    font-size: var(--fs-large);
    color: white;
    margin: 0;
}

#barBottom {
    position: absolute;
    left: 0;
    bottom: 0;
}
</style>