export { playersReady, makeInitialState, startGame, endTurn, endGame, game };

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

const game = new Game();

function playersReady(state) {
  console.dir(state);
  if (state.is_played === false) {
    console.log("CONDITION MET");
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
    console.log("Rendering Initial State");
    playersReady(game);
  }

  aquireInitialState(dataJson);
  renderInitialState(game);
  return game;
}

function startGame(dataJson) {
  game.is_played = true;
  console.log(game.is_played);
}

function endGame(dataJson) {
  console.log("endGame");
}

function endTurn(dataJson) {
  console.log("endTurn");
}
