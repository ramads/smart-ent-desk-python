-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 10, 2024 at 07:48 PM
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
  `id_riwayat` int(11) DEFAULT NULL,
  `diagnosa` varchar(255) NOT NULL,
  `tanggal_diagnosa` date NOT NULL,
  `hasil_diagnosa` text DEFAULT NULL,
  `tingkat_keyakinan` int(11) DEFAULT NULL,
  `gambar_diagnosa` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Diagnosa`
--

INSERT INTO `Diagnosa` (`id_diagnosa`, `id_riwayat`, `diagnosa`, `tanggal_diagnosa`, `hasil_diagnosa`, `tingkat_keyakinan`, `gambar_diagnosa`) VALUES
(1, 1, 'Otitis Media', '2024-01-15', 'Infeksi pada telinga tengah', 90, 'otitis_media.jpg'),
(2, 2, 'Sinusitis', '2024-02-20', 'Infeksi pada rongga sinus', 80, 'sinusitis.jpg'),
(3, 3, 'Tonsilitis', '2024-03-25', 'Peradangan pada amandel', 70, 'tonsilitis.jpg'),
(4, 1, 'Tinnitus', '2024-04-10', 'Telinga berdenging', 75, 'tinnitus.jpg'),
(5, 2, 'Rhinitis', '2024-05-05', 'Peradangan pada rongga hidung', 65, 'rhinitis.jpg'),
(6, 3, 'Faringitis', '2024-06-15', 'Radang tenggorokan', 92, 'faringitis.jpg'),
(8, 9, 'Aerotitis Barotrauma', '2024-07-11', '', 23, 'temp_image/1_9.jpg');

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
-- Table structure for table `Riwayat_Pemeriksaan`
--

CREATE TABLE `Riwayat_Pemeriksaan` (
  `id_riwayat` int(11) NOT NULL,
  `id_pasien` int(11) DEFAULT NULL,
  `id_rumah_sakit` int(11) DEFAULT NULL,
  `organ` enum('Telinga','Hidung','Tenggorokan') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Riwayat_Pemeriksaan`
--

INSERT INTO `Riwayat_Pemeriksaan` (`id_riwayat`, `id_pasien`, `id_rumah_sakit`, `organ`) VALUES
(1, 1, 1, 'Telinga'),
(2, 2, 1, 'Hidung'),
(3, 3, 2, 'Tenggorokan'),
(7, 1, 1, 'Telinga'),
(8, 1, 1, 'Telinga'),
(9, 1, 1, 'Telinga');

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
  ADD KEY `id_riwayat` (`id_riwayat`);

--
-- Indexes for table `Pasien`
--
ALTER TABLE `Pasien`
  ADD PRIMARY KEY (`id_pasien`);

--
-- Indexes for table `Riwayat_Pemeriksaan`
--
ALTER TABLE `Riwayat_Pemeriksaan`
  ADD PRIMARY KEY (`id_riwayat`),
  ADD KEY `id_rumah_sakit` (`id_rumah_sakit`),
  ADD KEY `id_pasien` (`id_pasien`);

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
  MODIFY `id_diagnosa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `Pasien`
--
ALTER TABLE `Pasien`
  MODIFY `id_pasien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Riwayat_Pemeriksaan`
--
ALTER TABLE `Riwayat_Pemeriksaan`
  MODIFY `id_riwayat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

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
  ADD CONSTRAINT `Diagnosa_ibfk_1` FOREIGN KEY (`id_riwayat`) REFERENCES `Riwayat_Pemeriksaan` (`id_riwayat`);

--
-- Constraints for table `Riwayat_Pemeriksaan`
--
ALTER TABLE `Riwayat_Pemeriksaan`
  ADD CONSTRAINT `Riwayat_Pemeriksaan_ibfk_1` FOREIGN KEY (`id_rumah_sakit`) REFERENCES `Rumah_Sakit` (`id_rumah_sakit`),
  ADD CONSTRAINT `Riwayat_Pemeriksaan_ibfk_2` FOREIGN KEY (`id_pasien`) REFERENCES `Pasien` (`id_pasien`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
