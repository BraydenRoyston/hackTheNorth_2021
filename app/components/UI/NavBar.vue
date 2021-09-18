<template>
    <nav>
        <div class="logoWrapper">
            <img src="../../static/robot.svg" alt="">
        </div>
        <div class="nav-links">
            <ul>
                <li>
                    <a href="#">Try it Out</a>
                </li>
                <li>
                    <a href="#">How it Works</a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<style scoped>
nav {
    width: 100vw;
    height: 10vh;

    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;

    position: absolute;
    top: 0;
    left: 0;
}

img {
    height: 10vh;
    width: auto;
    filter: invert(99%) sepia(100%) saturate(5%) hue-rotate(345deg) brightness(106%) contrast(100%);
}

p {
    font-family: var(--font-header);
    font-size: var(--fs-medium);
    color: white;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

li {
    font-size: var(--fs-small);
    padding: 10px;
}

a {
    font-family: var(--font-body);
    text-decoration: none;
    color: white;
}
</style>