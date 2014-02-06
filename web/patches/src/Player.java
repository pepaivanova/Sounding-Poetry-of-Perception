
import java.io.File;
import java.io.FileInputStream;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.SourceDataLine;

public class Player {

	public static void main(String[] args) throws Exception {
		if (args.length == 0) {
			System.out.println("Usage: java Player file");
			return;
		}
		AudioFormat format = new AudioFormat(44100.0f, 16, 2, true, false);
		DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
		if (!AudioSystem.isLineSupported(info)) {
			throw new Exception("Not supported");
		}
		SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
		line.open(format);
		File f = new File(args[0]);
		FileInputStream fin = new FileInputStream(f);
		byte[] buff = new byte[Math.max((int) f.length() - 84, 84)];
		fin.read(buff, 0, 84);
		fin.read(buff);
		fin.close();
		line.start();
		line.write(buff, 0, buff.length);
		line.stop();
		line.close();
		System.out.println("Done.");
	}
	
}
