import pygame

# Η κλάση κληρονομεί όλες τις ιδιότητες και μεθόδους της κλάσης  "Sprite" που ανήκει στη Pygame.
class Ρακέτα(pygame.sprite.Sprite):

    def __init__(self, color, πλάτος, ύψος, maxy):
        # καλούμε την __init__ της κλάσης Sprite
        super().__init__()

        # Η μεγαλύτερη απόσταση που μπορεί να έχει η ρακέτα από το πάνω μέρος του παραθύρου
        self.maxy=maxy
        # Δημιουργεί ένα καμβά στον οποίο θα ζωγραφίσει ένα παραλληλόγραμμο (ρακέτα)
        self.image = pygame.Surface([πλάτος, ύψος])
        # Καθορίζει το χρώμα του καμβά
        self.image.fill((0, 0, 0))
        # Κάνει το χρώμα του καμβά διαφανές
        self.image.set_colorkey((0, 0, 0))

        # Ζωγραφίζει ένα παραλληλόγραμμο μέσα στον καμβά
        pygame.draw.rect(self.image, color, [0, 0, πλάτος, ύψος])

        # Το παραλληλόγραμμο του καμβά
        self.rect = self.image.get_rect()

    def ρακέτα_πάνω(self, pixels):
        self.rect.y -= pixels
        # Δεν πρέπει η ρακέτα κατά την ανοδική κίνσηση να βγεί εκτός παραθύρου
        if self.rect.y < 0:
            self.rect.y = 0

    def ρακέτα_κάτω(self, pixels):
        self.rect.y += pixels
        # Δεν πρέπει η ρακέτα κατά την καθοδική  κίνσηση να βγεί εκτός παραθύρου
        if self.rect.y > self.maxy:
            self.rect.y = self.maxy

