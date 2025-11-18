import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# -----------------------------
# データ読み込み
# -----------------------------
def load_data(file_path):
    """テキストファイルを読み込み、NumPy配列を返す"""
    with open(file_path, "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        row = line.strip().split()
        data.append(row)

    data = np.array(data, dtype=float)
    return data


# -----------------------------
# DC成分除去
# -----------------------------
def remove_dc(signal):
    """直流成分（平均値）を除去した信号と、元の平均値を返す"""
    dc_component = np.mean(signal)
    signal_without_dc = signal - dc_component
    return signal_without_dc, dc_component


# -----------------------------
# FFTとパワースペクトル
# -----------------------------
def compute_fft(signal_without_dc, time):
    """直流成分除去済み信号と時間配列から、周波数とパワースペクトルを計算"""
    sampling_interval = time[1] - time[0]
    fs = 1.0 / sampling_interval

    fft_result = np.fft.fft(signal_without_dc)
    fft_freqs = np.fft.fftfreq(len(fft_result), 1 / fs)

    power_spectrum = np.abs(fft_result)  # 元のコードと同じ定義（振幅）

    # 正の周波数だけ抽出
    mask = fft_freqs >= 0
    positive_freqs = fft_freqs[mask]
    positive_spectrum = power_spectrum[mask]

    return positive_freqs, positive_spectrum


# -----------------------------
# ピーク検出
# -----------------------------
def detect_peaks(freqs, spectrum, height=0.0):
    """パワースペクトルからピークを検出して、その周波数と値を返す"""
    peaks, _ = find_peaks(spectrum, height=height)
    peak_freqs = freqs[peaks]
    peak_values = spectrum[peaks]
    return peak_freqs, peak_values


# -----------------------------
# プロット
# -----------------------------
def plot_results(time, signal, freqs, spectrum, peak_freqs, peak_values, fmin, fmax):
    """入力信号とフーリエ変換結果をプロットする"""
    plt.figure(figsize=(12, 6))

    # 入力信号
    plt.subplot(2, 1, 1)
    plt.plot(time, signal)
    plt.title("Input Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("K")

    # FFT結果
    plt.subplot(2, 1, 2)
    plt.plot(freqs, spectrum)
    # plt.plot(peak_freqs, peak_values, "ro")  # ピークを表示したい場合
    plt.title("Fourier Transform Result (After Removing DC Component)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectrum")

    # 周波数表示範囲をユーザー指定に
    plt.xlim(fmin, fmax)

    plt.tight_layout()
    plt.show()


# -----------------------------
# main
# -----------------------------
def main():
    """ユーザー入力でファイルパスと周波数範囲を受け取り解析を実行"""

    # -------------------------
    # ファイルパス入力
    # -------------------------
    file_path = input("解析したいデータファイル（.txt）のパスを入力してください：\n> ")

    try:
        data = load_data(file_path)
    except Exception as e:
        print(f"\n[エラー] ファイルを読み込めませんでした： {e}")
        return

    # データ抽出
    time = data[:, 0]
    signal = data[:, 1]

    # -------------------------
    # 周波数範囲入力
    # -------------------------
    print("\n周波数表示範囲を設定してください（例：0 400）")
    print("そのまま Enter を押すとデフォルト値 (0.01, 400) を使います。")

    user_input = input("fmin fmax > ")

    if user_input.strip() == "":
        fmin, fmax = 0.01, 400
    else:
        try:
            fmin, fmax = map(float, user_input.split())
        except:
            print("[警告] 入力形式が正しくありません。デフォルト値を使用します。")
            fmin, fmax = 0.01, 400

    # -------------------------
    # FFT 処理
    # -------------------------
    signal_wo_dc, _ = remove_dc(signal)
    freqs, spectrum = compute_fft(signal_wo_dc, time)
    peak_freqs, peak_values = detect_peaks(freqs, spectrum)

    # -------------------------
    # ピーク表示
    # -------------------------
    print("\nピーク周波数とその値:")
    for f, v in zip(peak_freqs, peak_values):
        print(f"周波数: {f:.4f} Hz, 値: {v:.4e}")

    # -------------------------
    # プロット
    # -------------------------
    plot_results(time, signal, freqs, spectrum, peak_freqs, peak_values, fmin, fmax)


# -----------------------------
if __name__ == "__main__":
    main()

