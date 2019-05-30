# Created by Adam at 5/30/2019
Feature: dual_rootfs
  Determine and set the state of the rootfs partition

  Scenario: get boot rootfs device
    Given the sample cmdline file mmcblk0p1
    When we query the boot rootfs device
    Then the reported boot rootfs device is /dev/mmcblk0p1