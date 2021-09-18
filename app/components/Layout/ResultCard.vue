<template>
    <div class="result">
        <ul>
            <li>
                <p class="name main-name">Overall Score</p>
                <div class="grade main-grade">
                    <p class="score main-score">10</p>
                </div>
            </li>
            <li>
                <p class="name">Rhyme Score</p>
                <div class="grade">
                    <p class="score">10</p>
                </div>
            </li>
            <li>
                <p class="name">Semantic Score</p>
                <div class="grade">
                    <p class="score">10</p>
                </div>
            </li>
            <li>
                <p class="name">Repetitiveness Score</p>
                <div class="grade">
                    <p class="score">10</p>
                </div>
            </li>
        </ul>
    </div>
</template>


<style scoped>
.result {
    height: 60vh;
    width: 60vh;

    /* background: white; */
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    padding: 10px;
    margin: 5px;

    width: 100%;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.name {
    font-size: var(--fs-medium);
    font-family: var(--font-body);
    color: white;

    transition: all 1s ease;
}

.grade {
    margin: 5px;

    display: flex;
    justify-content: center;
    align-items: center;

    border: 1px solid white;
    background: transparent;
    border-radius: 50%;
    height: 5vh;
    width: 5vh;

    transition: all 1s ease;
}

li:hover .grade {
    border: 1px solid var(--light-blue);
}

li:hover .grade p {
    color: var(--light-blue);
}

li:hover .name {
    color: var(--light-blue);
}

.score {
    margin: 5px;

    font-size: var(--fs-medium);
    color: white;
    font-family: var(--font-body);

    transition: all 1s ease;
}

.main-name {
    font-size: var(--fs-large);
    color: var(--light-blue);
}

.main-grade {
    height: 8vh;
    width: 8vh;
    border-color: var(--light-blue);
}

.main-score {
    font-size: var(--fs-large);
    color: var(--light-blue);
}
</style>