<template>
    <div class="wrapper">
        <div class="bar" id="a"></div>
        <div class="bar" id="b"></div>
        <div class="bar" id="c"></div>
        <div class="bar" id="d"></div>
        <div class="bar" id="e"></div>
        <div class="bar" id="f"></div>
        <div class="bar" id="g"></div>
        <div class="bar" id="h"></div>
        <div class="bar" id="i"></div>
        <div class="bar" id="j"></div>
    </div>
</template>


<style scoped>
.wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;

    height: 20vh;
    width: 100vw;
}

.bar {
    height: 100%;
    width: 8vw;
    margin-right: 1vw;
    margin-left: 1vw;
}

#a {
    animation: barBounceHigh 2s linear infinite;
    background: white;
}

#b {
    animation: barBounce 1s ease-in infinite;
    background: var(--light-blue);
}

#c {
    animation: barBounceHigh 1s linear infinite;
    background: var(--blue);
}

#d {
    animation: barBounceLow 0.5s linear infinite;
    background: white;
}

#e {
    animation: barBounce 1s linear infinite;
    background: var(--light-blue);
}

#f {
    animation: barBounceHigh 2s linear infinite;
    background: var(--blue);
}

#g {
    animation: barBounce 1s ease-out infinite;
    background: var(--light-blue);
}

#h {
    animation: barBounceLow 0.75s linear infinite;
    background: white;
}

#i {
    animation: barBounce 2s linear infinite;
    background: var(--light-blue);
}

#j {
    animation: barBounceHigh 1s linear infinite;
    background: var(--blue);
}

@keyframes barBounce {
    0% {
        height: 0%
    }
    50% {
        height: 80%;
    }
    100% {
        height: 0%;
    }
}

@keyframes barBounceHigh {
    0% {
        height: 0%
    }
    50% {
        height: 120%;
    }
    100% {
        height: 0%;
    }
}

@keyframes barBounceLow {
    0% {
        height: 0%
    }
    50% {
        height: 40%;
    }
    100% {
        height: 0%;
    }
}


</style>