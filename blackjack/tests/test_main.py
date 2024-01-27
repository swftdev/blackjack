from blackjack import Player, Deck, Blackjack

class TestPlayer:
    def test_init(self):
        player = Player("Justin")

        assert player.hand == []
        assert player.name == "Justin"

    def test_addToHand(self):
        player = Player("Justin")
        card = ("King", "Spades")
        player.addToHand(card)

        assert card in player.hand

    def test_resetHand(self):
        player = Player("Justin")
        card = ("King", "Spades")
        player.addToHand(card)
        player.resetHand()

        assert len(player.hand) == 0

class TestDeck:
    def test_init(self):
        deck = Deck()
        assert len(deck._deck) == 52

    def test_shuffle(self):
        deck = Deck()
        before = deck._deck.copy()
        deck.shuffle()
        after = deck._deck

        assert before != after

    def test_deal(self):
        deck = Deck()
        c1 = deck.deal()
        c2 = deck.deal()

        assert len(deck._deck) == 50
        assert c1 != c2

    def test_reset(self):
        d1 = Deck()
        d2 = Deck()

        d1.shuffle()
        d1.deal()
        d1.reset()

        assert len(d1._deck) == 52
        assert d1._deck == d2._deck

class TestBlackjack:
    def test_new_blackjack_game_has_players(self):
        player1 = Player("Justin")
        game = Blackjack([player1])
        assert game.players.count(player1) == 1

    def test_initial_deal(self):
        player1 = Player("Justin")
        game = Blackjack([player1])
        game.initialDeal()
        for p in game.players:
            assert len(p.hand) == 2

        assert len(game.dealer.hand) == 2


# Test all methods that are not tested
# Test that after you start a blackjack game 
    # you can play a whole player hand
# Test that after the players turn ends it goes to the next player
