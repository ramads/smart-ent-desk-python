-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 12, 2024 at 10:21 AM
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

--
-- Dumping data for table `Diagnosa`
--

INSERT INTO `Diagnosa` (`id_diagnosa`, `diagnosa`, `tanggal_diagnosa`, `hasil_diagnosa`, `tingkat_keyakinan`, `gambar_diagnosa`, `prediksi_benar`, `alasan_koreksi`, `jenis_diagnosa`, `id_pasien`, `id_rumah_sakit`) VALUES
(21, 'OMed Efusi', '2024-07-12', 'Otitis Media dengan efusi, yaitu adanya cairan di telinga tengah tanpa adanya infeksi akut.', 23, 'temp_image/1_1_20240712_152757.jpg', 1, 'None', 'telinga', 1, 1),
(22, 'Aerotitis Barotrauma', '2024-07-12', 'Kondisi yang disebabkan oleh perbedaan tekanan antara telinga tengah dan lingkungan sekitarnya, sering terjadi saat naik atau turun pesawat.', 50, 'temp_image/2_1_20240712_152921.jpg', 1, 'None', 'telinga', 2, 1);

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
  MODIFY `id_diagnosa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

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
