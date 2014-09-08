
//import java.io.BufferedReader;
//import java.io.InputStreamReader;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.SourceDataLine;

public class AudioMix {

	public static void main(String[] args) throws Exception {
		if (args.length != 3 || args[1].length() == 0) {
			System.out.println("Usage: java AudioMix \"background\" <backgnd-coeff> \"message\"");
			return;
		}
		long start = System.currentTimeMillis();
		String background = args[0];
		double coeff;
		try {
			coeff = Double.parseDouble(args[1]);
		} catch (NumberFormatException ex) {
			System.err.println("Background volume coeffitient should be a floting-point number");
			return;
		}
		String message = args[2];
		byte[] buff = mixWords(getWords(message));
		if (buff == null) {
			System.out.println("Nothing to play.");
			return;
		}
		byte[] backgroundBuff = null;
		byte[] back = mixWords(getWords(background));

		if (back != null) {
			backgroundBuff = new byte[back.length];
			System.arraycopy(back, 0, backgroundBuff, 0, back.length);
			while (backgroundBuff.length < buff.length) {
				backgroundBuff = mixWithOverlap(backgroundBuff, back);
			}
		}
		
		if (backgroundBuff != null) {
			backgroundBuff = cut(backgroundBuff, buff.length);
			buff = mix(buff, adjustVolume(backgroundBuff, coeff));
		}
		
//		System.out.println("Generated in " + (System.currentTimeMillis() - start) + " ms.");

		AudioFormat format = new AudioFormat(44100.0f, 16, 2, true, false);
		DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
		if (!AudioSystem.isLineSupported(info)) {
			throw new Exception("Not supported");
		}
		SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
		line.open(format);
		line.start();
		line.write(buff, 0, buff.length / 4 * 4);
		line.stop();
		line.close();
		System.out.println("Done.");
	}

	private static ArrayList<String> getWords(String s) {
		ArrayList<String> words = new ArrayList<String>();
		int wordStart = -1;
		for (int i = 0; i < s.length(); i++) {
			if (Character.isLetterOrDigit(s.charAt(i))) {
				if (wordStart < 0) {
					wordStart = i;
				}
			} else {
				if (wordStart >= 0) {
					words.add(s.substring(wordStart, i));
					wordStart = -1;
				}
			}
		}
		if (wordStart >= 0) {
			words.add(s.substring(wordStart, s.length()));
		}
		return words;
	}

	private static byte[] mixWords(ArrayList<String> words) throws Exception {
		byte[] buff = null;
		for (String filename: words) {
			File f = new File("sounds/" + filename + ".wav");
			if (f.exists()) {
//				System.out.print(filename + ' ');
				if (buff == null) {
					buff = readSamples(f.getAbsolutePath());
				} else {
					buff = mixWithOverlap(buff, readSamples(f.getAbsolutePath()));
				}
			}
		}
		return buff;
	}

	private static byte[] readSamples(String filename) throws Exception {
		return readSamples(filename, true, true);
	}

	private static byte[] readSamples(String filename, boolean fadeIn, boolean fadeOut) throws Exception {
		File f = new File(filename);
		FileInputStream fin = new FileInputStream(f);
		byte[] buff = new byte[Math.max((int) f.length() - 84, 84)];
		fin.read(buff, 0, 84);
		fin.read(buff);
		fin.close();

		int max = Math.min(buff.length / 2 / 3 * 2, 44100 * 4); // 1/3 of sound's time or max 1s.
		if (fadeIn) {
			for (int i = 0; i < max && i < buff.length; i += 2) {
				int sample = ((buff[i + 1] & 0xff) << 8) | (buff[i] & 0xff);
				if (sample > 32767) {
					sample -= 65536;
				}
				sample = (int) ((long) sample * i * i / max / max);
				buff[i] = (byte) sample;
				buff[i + 1] = (byte) (sample >> 8);
			}
		}

		if (fadeOut) {
			for (int i = buff.length - max, j = max - 1; i < buff.length; i += 2, j -= 2) {
				int sample = ((buff[i + 1] & 0xff) << 8) | (buff[i] & 0xff);
				if (sample > 32767) {
					sample -= 65536;
				}
				sample = (int) ((long) sample * j * j / max / max);
				buff[i] = (byte) sample;
				buff[i + 1] = (byte) (sample >> 8);
			}
		}
		
		return buff;
	}
	
	private static byte[] mixWithOverlap(byte[] buff1, byte[] buff2) {
		int fade = Math.min(buff2.length / 2 / 3 * 2, 44100 * 4 * 1); // Fade in/out is one third of the play time or 1s (the less of the two times).
		byte[] res = new byte[buff1.length + buff2.length - fade];
		System.arraycopy(buff1, 0, res, 0, buff1.length);
		System.arraycopy(buff2, fade, res, buff1.length, buff2.length - fade);
		int offset = buff1.length - fade;
		if (offset < 0) {
			offset = 0;
		}
		for (int i = 0; i < fade; i += 2) {
			int index1 = offset + i;
			int sample1 = index1 < buff1.length ? ((buff1[index1 + 1] & 0xff) << 8) | (buff1[index1] & 0xff) : 0;
			if (sample1 > 32767) {
				sample1 -= 65536;
			}
			int sample2 = ((buff2[i + 1] & 0xff) << 8) | (buff2[i] & 0xff);
			if (sample2 > 32767) {
				sample2 -= 65536;
			}
			int sample = sample1 + sample2;
			if (sample > 32767) {
				sample = 32767;
			}
			if (sample < -32768) {
				sample = -32768;
			}
			res[index1] = (byte) sample;
			res[index1 + 1] = (byte) (sample >> 8);
		}
		return res;
	}

	private static byte[] mix(byte[] buff1, byte[] buff2) {
		byte[] res = new byte[Math.max(buff1.length, buff2.length)];
		for (int i = 0; i < res.length; i += 2) {
			int sample1 = i < buff1.length ? ((buff1[i + 1] & 0xff) << 8) | (buff1[i] & 0xff) : 0;
			if (sample1 > 32767) {
				sample1 -= 65536;
			}
			int sample2 = i < buff2.length ? ((buff2[i + 1] & 0xff) << 8) | (buff2[i] & 0xff) : 0;
			if (sample2 > 32767) {
				sample2 -= 65536;
			}
			int sample = sample1 + sample2;
			if (sample > 32767) {
				sample = 32767;
			}
			if (sample < -32768) {
				sample = -32768;
			}
			res[i] = (byte) sample;
			res[i + 1] = (byte) (sample >> 8);
		}
		return res;
	}

	private static byte[] adjustVolume(byte[] buff, double coeff) {
		for (int i = 0; i < buff.length; i += 2) {
			int sample = ((buff[i + 1] & 0xff) << 8) | (buff[i] & 0xff);
			if (sample > 32767) {
				sample -= 65536;
			}
			sample = (int) (sample * coeff);
			buff[i] = (byte) sample;
			buff[i + 1] = (byte) (sample >> 8);
		}
		return buff;
	}

	private static byte[] cut(byte[] buff, int length) {
		byte[] res = new byte[length];
		System.arraycopy(buff, 0, res, 0, res.length);
		return res;
	}

}