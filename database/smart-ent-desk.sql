-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 26, 2024 at 08:13 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smart-ent-desk`
--

-- --------------------------------------------------------

--
-- Table structure for table `Asuransi`
--

CREATE TABLE `Asuransi` (
  `id_asuransi` int(11) NOT NULL,
  `id_pasien` int(11) DEFAULT NULL,
  `nama_asuransi` varchar(255) NOT NULL,
  `nomor_asuransi` varchar(255) NOT NULL,
  `jenis_asuransi` varchar(255) DEFAULT NULL,
  `fasilitas_kesehatan` varchar(255) DEFAULT NULL,
  `kelas_asuransi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Asuransi`
--

INSERT INTO `Asuransi` (`id_asuransi`, `id_pasien`, `nama_asuransi`, `nomor_asuransi`, `jenis_asuransi`, `fasilitas_kesehatan`, `kelas_asuransi`) VALUES
(1, 1, 'Asuransi Sehat', 'AS123456', 'BPJS', 'Rumah Sakit Umum', 'VIP'),
(2, 2, 'Asuransi Aman', 'AA654321', 'BPJS', 'Rumah Sakit Khusus', 'Kelas I'),
(3, 3, 'Asuransi Prima', 'AP112233', 'Swasta', 'Klinik', 'Kelas II');

-- --------------------------------------------------------

--
-- Table structure for table `Diagnosa`
--

CREATE TABLE `Diagnosa` (
  `id_diagnosa` int(11) NOT NULL,
  `diagnosa` varchar(255) NOT NULL,
  `tanggal_diagnosa` date NOT NULL,
  `hasil_diagnosa` text DEFAULT NULL,
  `tingkat_keyakinan` int(11) DEFAULT NULL,
  `gambar_diagnosa` varchar(255) DEFAULT NULL,
  `prediksi_benar` tinyint(1) DEFAULT NULL,
  `alasan_koreksi` text DEFAULT NULL,
  `jenis_diagnosa` enum('telinga','hidung','tenggorokan') DEFAULT NULL,
  `id_pasien` int(11) DEFAULT NULL,
  `id_rumah_sakit` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Notifikasi`
--

CREATE TABLE `Notifikasi` (
  `id_notifikasi` int(11) NOT NULL,
  `notif_header` varchar(255) DEFAULT NULL,
  `notif_subheader` varchar(255) DEFAULT NULL,
  `notif_content` text DEFAULT NULL,
  `already_read` tinyint(1) DEFAULT NULL,
  `notif_datetime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Notifikasi`
--

INSERT INTO `Notifikasi` (`id_notifikasi`, `notif_header`, `notif_subheader`, `notif_content`, `already_read`, `notif_datetime`) VALUES
(11, 'Peringatan Diagnosa', 'Tingkat Kritis', 'Pasien menunjukkan gejala infeksi tenggorokan yang parah. Segera lakukan pemeriksaan lebih lanjut.', 0, '2024-07-26 08:45:00'),
(12, 'Update Kasus', 'Pemeriksaan Lengkap', 'Kasus pasien John Doe telah diperbarui dengan hasil laboratorium terbaru. Mohon periksa laporan.', 1, '2024-07-26 09:30:00'),
(13, 'Reminder', 'Jadwal Konsultasi', 'Jangan lupa jadwal konsultasi dengan pasien Jane Smith pada pukul 11:00 hari ini.', 1, '2024-07-26 10:00:00'),
(14, 'Notifikasi Sistem', 'Pembaruan Versi', 'Aplikasi telah diperbarui ke versi terbaru. Mohon restart aplikasi untuk menerapkan perubahan.', 1, '2024-07-26 11:00:00'),
(15, 'Peringatan Diagnosa', 'Gejala Baru', 'Pasien baru dengan gejala sinusitis. Segera lakukan pemeriksaan.', 0, '2024-07-25 14:15:00'),
(16, 'Update Kasus', 'Histori Medis', 'Pasien Mary Johnson telah mengunggah histori medis terbarunya.', 1, '2024-07-24 16:45:00'),
(17, 'Reminder', 'Jadwal Operasi', 'Jadwal operasi pasien Michael Brown pada pukul 15:00 besok.', 0, '2024-07-23 17:00:00'),
(18, 'Notifikasi Sistem', 'Maintenance Server', 'Server akan menjalani pemeliharaan rutin pada 2024-07-22 mulai pukul 02:00 hingga 04:00.', 1, '2024-07-21 12:30:00'),
(19, 'Peringatan Diagnosa', 'Alergi', 'Pasien dengan alergi berat terhadap obat-obatan tertentu. Periksa detail lebih lanjut.', 0, '2024-07-20 08:00:00'),
(20, 'Update Kasus', 'Hasil Pemeriksaan', 'Hasil pemeriksaan pasien David Wilson telah tersedia. Mohon periksa laporan.', 1, '2024-07-19 09:45:00'),
(21, 'Reminder', 'Vaksinasi', 'Pasien Sarah Davis dijadwalkan untuk vaksinasi pada 2024-07-18 pukul 14:00.', 0, '2024-07-17 10:15:00'),
(22, 'Notifikasi Sistem', 'Fitur Baru', 'Fitur baru telah ditambahkan ke aplikasi. Baca dokumentasi untuk informasi lebih lanjut.', 1, '2024-07-16 13:00:00'),
(23, 'Peringatan Diagnosa', 'Kondisi Darurat', 'Pasien mengalami kesulitan bernapas. Segera lakukan tindakan darurat.', 0, '2024-07-15 07:30:00'),
(24, 'Update Kasus', 'Rekomendasi Dokter', 'Dokter merekomendasikan pemeriksaan lanjutan untuk pasien Emma Thomas.', 1, '2024-07-14 10:00:00'),
(25, 'Reminder', 'Konsultasi Online', 'Konsultasi online dengan pasien James Lee dijadwalkan pada 2024-07-13 pukul 13:30.', 0, '2024-07-12 11:00:00'),
(26, 'Notifikasi Sistem', 'Keamanan Data', 'Pembaruan keamanan telah diterapkan. Mohon restart aplikasi.', 1, '2024-07-11 12:45:00');

-- --------------------------------------------------------

--
-- Table structure for table `Pasien`
--

CREATE TABLE `Pasien` (
  `id_pasien` int(11) NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Pasien`
--

INSERT INTO `Pasien` (`id_pasien`, `nama_pasien`, `jenis_kelamin`, `tanggal_lahir`, `alamat`) VALUES
(1, 'John Doe', 'Laki-laki', '1980-05-15', 'Jl. Kebon Jeruk No. 3'),
(2, 'Jane Smith', 'Perempuan', '1992-08-25', 'Jl. Mangga Dua No. 5'),
(3, 'Michael Johnson', 'Laki-laki', '1975-11-10', 'Jl. Karet No. 7');

-- --------------------------------------------------------

--
-- Table structure for table `Rumah_Sakit`
--

CREATE TABLE `Rumah_Sakit` (
  `id_rumah_sakit` int(11) NOT NULL,
  `nama_rumah_sakit` varchar(255) NOT NULL,
  `alamat_rumah_sakit` text NOT NULL,
  `phone_number_rumah_sakit` varchar(20) DEFAULT NULL,
  `email_rumah_sakit` varchar(255) DEFAULT NULL,
  `situs_rumah_sakit` varchar(255) DEFAULT NULL,
  `tentang_rumah_sakit` varchar(255) DEFAULT NULL,
  `jumlah_partner` int(11) DEFAULT NULL,
  `jumlah_award` int(11) DEFAULT NULL,
  `jumlah_tenang_ahli` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Rumah_Sakit`
--

INSERT INTO `Rumah_Sakit` (`id_rumah_sakit`, `nama_rumah_sakit`, `alamat_rumah_sakit`, `phone_number_rumah_sakit`, `email_rumah_sakit`, `situs_rumah_sakit`, `tentang_rumah_sakit`, `jumlah_partner`, `jumlah_award`, `jumlah_tenang_ahli`) VALUES
(1, 'Rumah Sakit ABC', 'Jl. Merdeka No. 1', '021-12345678', 'contact@rsabc.com', 'www.rsabc.com', 'Rumah Sakit terbaik di kota', 20, 5, 100),
(2, 'Rumah Sakit XYZ', 'Jl. Sudirman No. 2', '021-87654321', 'info@rsxyz.com', 'www.rsxyz.com', 'Pelayanan terbaik dan cepat', 30, 10, 200);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Asuransi`
--
ALTER TABLE `Asuransi`
  ADD PRIMARY KEY (`id_asuransi`),
  ADD KEY `id_pasien` (`id_pasien`);

--
-- Indexes for table `Diagnosa`
--
ALTER TABLE `Diagnosa`
  ADD PRIMARY KEY (`id_diagnosa`),
  ADD KEY `Diagnosa_Pasien_id_pasien_fk` (`id_pasien`),
  ADD KEY `Diagnosa_Rumah_Sakit_id_rumah_sakit_fk` (`id_rumah_sakit`);

--
-- Indexes for table `Notifikasi`
--
ALTER TABLE `Notifikasi`
  ADD PRIMARY KEY (`id_notifikasi`);

--
-- Indexes for table `Pasien`
--
ALTER TABLE `Pasien`
  ADD PRIMARY KEY (`id_pasien`);

--
-- Indexes for table `Rumah_Sakit`
--
ALTER TABLE `Rumah_Sakit`
  ADD PRIMARY KEY (`id_rumah_sakit`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Asuransi`
--
ALTER TABLE `Asuransi`
  MODIFY `id_asuransi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Diagnosa`
--
ALTER TABLE `Diagnosa`
  MODIFY `id_diagnosa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `Notifikasi`
--
ALTER TABLE `Notifikasi`
  MODIFY `id_notifikasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `Pasien`
--
ALTER TABLE `Pasien`
  MODIFY `id_pasien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Rumah_Sakit`
--
ALTER TABLE `Rumah_Sakit`
  MODIFY `id_rumah_sakit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Asuransi`
--
ALTER TABLE `Asuransi`
  ADD CONSTRAINT `Asuransi_ibfk_1` FOREIGN KEY (`id_pasien`) REFERENCES `Pasien` (`id_pasien`);

--
-- Constraints for table `Diagnosa`
--
ALTER TABLE `Diagnosa`
  ADD CONSTRAINT `Diagnosa_Pasien_id_pasien_fk` FOREIGN KEY (`id_pasien`) REFERENCES `Pasien` (`id_pasien`),
  ADD CONSTRAINT `Diagnosa_Rumah_Sakit_id_rumah_sakit_fk` FOREIGN KEY (`id_rumah_sakit`) REFERENCES `Rumah_Sakit` (`id_rumah_sakit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
