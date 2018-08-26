import org.jfugue.player.Player;
import org.jfugue.midi.MidiFileManager;
import org.jfugue.pattern.Pattern;
import java.io.File;
import java.io.IOException;

public class violin {
    public static void main(String[] args) {

        Pattern init = new Pattern("C D E");
        Pattern p0 = new Pattern(" T[Allegro] V0 I[Guitar] KEmaj G6i G6i G6i F6s E6s B6q. B6s A6s");

        Player player = new Player();
        player.play(p0);


    }

}

