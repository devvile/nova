export {
  playersReady,
  makeInitialState,
  startGame,
  endTurn,
  endGame,
  rollDice,
  refreshGame,
  setState,
  makeMove,
  game,
  Player,
};

import { prepareBoard } from "./board.js";

//CLASSES

class Game {
  constructor(
    name,
    host,
    is_played,
    who_is_ready,
    max_players,
    turn,
    turn_of_player
  ) {
    this.name = name;
    this.host = host;
    this.is_played = is_played;
    this.who_is_ready = who_is_ready;
    this.max_players = max_players;
    this.turn = turn;
    this.turn_of_player = turn_of_player;
  }
}

class Board {
  constructor(...args) {
    this.fields = args[0];
  }
}

class Player {
  constructor(name, color, money, position, moved, estates, playing) {
    this.name = name;
    this.color = color;
    this.money = money;
    this.position = position;
    this.moved = moved;
    this.estates = estates;
    this.playing = playing;
  }
}

//bycmoze trzeba dac funkcje jako metody

const game = new Game();

function makeMove(player, fileds_to_move) {
  let old_field = document.getElementById(player.position);
  old_field.style.backgroundColor = "grey";
  let new_poss = player.position + fileds_to_move;
  if (new_poss >= 28) {
    new_poss -= 28;
  }
  player.position = new_poss;
  let color = player.color;

  renderMove();
  function renderMove() {
    console.log("position" + player.position);
    let new_field = document.getElementById(player.position);
    new_field.style.backgroundColor = color;
  }
}

function playersReady(state) {
  if (state.is_played === false) {
    const playersReadyText = document.querySelector(".players_ready_text");
    playersReadyText.textContent = `Players ready: ${state.who_is_ready}`;
  } else {
    console.log("GAME ALREADY STARTED CANNOT MAKE PLAYER READY");
  }
}

function makeInitialState(dataJson) {
  function aquireInitialState(dataJson) {
    (game.name = dataJson.name),
      (game.is_played = dataJson.is_played),
      (game.host = dataJson.host),
      (game.who_is_ready = dataJson.who_is_ready),
      (game.who_is_playing = dataJson.who_is_playing),
      (game.max_players = dataJson.max_players),
      (game.turn = dataJson.turn),
      (game.turn_of_player = dataJson.turn_of_player);
  }

  function renderInitialState(game) {
    gameRender(game);
  }

  function prepareFields(dataJson) {
    let fields = JSON.parse(dataJson.mess);
    const board = new Board(fields);
    return board;
  }

  aquireInitialState(dataJson);
  renderInitialState(game);
  let boardFields = prepareFields(dataJson);
  prepareBoard();

  return boardFields;
}

function gameRender(game) {
  if (game.is_played === true) {
    makeVisible();
  } else {
    makeInvisible();
  }
  playersReady(game);
}

function startGame(dataJson) {
  makeVisible();
  game.turn_of_player = dataJson.turn_of_player;
  game.who_is_playing = dataJson.who_is_playing;
  game.is_played = true;
  refreshPlayers(dataJson);
  console.log("Game starting");
}

function refreshPlayers(game) {
  const playerTurnText = document.querySelector(".player_turn_text");
  const playersInGame = document.querySelector(".players_in_game");

  playerTurnText.textContent = ` ${game.turn_of_player} turn!`;
  playersInGame.textContent = ` Players in game: ${game.who_is_playing}`;
}

function endGame(dataJson) {
  makeInvisible();
  game.is_played = false;
  console.log("endGame");
}

async function setState(game) {
  console.dir(game);
  refreshPlayers(game);
}

function refreshGame(dataJson) {
  {
    (game.name = dataJson.name),
      (game.is_played = dataJson.is_played),
      (game.host = dataJson.host),
      (game.who_is_ready = dataJson.who_is_ready),
      (game.who_is_playing = dataJson.who_is_playing),
      (game.max_players = dataJson.max_players),
      (game.turn = dataJson.turn),
      (game.turn_of_player = dataJson.turn_of_player);
  }
}

function endTurn(state) {
  console.log("halo" + state.turn_of_player);
  setTimeout(setState, 200, state);
}
function rollDice(dataJson) {
  console.log("rollDice");
}

function makeVisible() {
  const gamePlayed = document.querySelector(".--game_state");
  const visList = document.querySelectorAll(".--vis");
  const inVisList = document.querySelectorAll(".--invis");
  const menu = document.querySelector(".__sidebar_menu_column");

  gamePlayed.textContent = " GAME ALREADY STARTED!";

  visList.forEach((elem) => (elem.style.display = "none"));
  inVisList.forEach((elem) => (elem.style.display = "block"));
  menu.style.display = "flex";

  refreshPlayers(game);
}

function makeInvisible() {
  const visList = document.querySelectorAll(".--vis");
  const inVisList = document.querySelectorAll(".--invis");
  const gamePlayed = document.querySelector(".--game_state");

  gamePlayed.textContent = " GAME HASN'T STARTED YET!";
  visList.forEach((elem) => (elem.style.display = "block"));
  inVisList.forEach((elem) => (elem.style.display = "none"));
}
